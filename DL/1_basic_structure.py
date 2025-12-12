'''
딥러닝에서는 데이터(Data), 모델(Model), 학습 과정(Training)이
서로 강하게 결합되어 있다.
데이터 분포나 전처리가 바뀌면 모델의 의미가 달라지고,
모델 구조가 바뀌면 학습 안정성과 최적화 방식이 달라지며,
학습 과정이 달라지면 같은 모델이라도 전혀 다른 함수가 된다.

이 세 요소를 명확히 분리하지 않으면
어떤 변경이 성능 변화의 원인인지 추적할 수 없고,
실험 비교, 코드 확장, 결과 재현이 모두 어려워진다.

그래서 딥러닝 코드는 다음 세 가지를 뼈대로 구성한다.

1. Dataset / DataLoader
   - 데이터 한 샘플의 정의와 전처리를 담당한다.
   - 배치 구성, 셔플, 병렬 로딩 등 데이터 공급 방식을 분리한다.

2. Model (nn.Module)
   - 입력을 출력으로 매핑하는 함수 근사를 정의한다.
   - 네트워크 구조와 학습 가능한 파라미터를 캡슐화한다.

3. Trainer
   - 학습 및 평가 루프를 관리한다.
   - loss 계산, backward, optimizer step,
     logging, checkpoint, 재현성을 통제한다.

딥러닝에서 좋은 코드는
단순히 성능이 좋은 코드가 아니라,
‘무엇을 바꿨고, 왜 결과가 달라졌는지’를
정확히 설명할 수 있는 코드다.

따라서 딥러닝에서 구조란
성능을 올리기 위한 장식이 아니라,
실험 결과를 신뢰하기 위해 반드시 필요한 기반이다.


딥러닝 최소 기본형 (Single-file version)

구성:
1) Dataset      : 데이터 한 샘플 정의
2) DataLoader  : 배치 단위로 데이터 공급
3) Model       : nn.Module (신경망 구조)
4) Trainer     : 학습 / 평가 과정 관리
5) main logic  : 실험 설정 및 실행


'''

# ===============================
# 0. 라이브러리 import
# ===============================
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

import pandas as pd
from sklearn.model_selection import train_test_split


# ===============================
# 1. Dataset 정의
# ===============================
class HeroDataset(Dataset):
    """
    PyTorch Dataset은 반드시
    - __len__
    - __getitem__
    을 구현해야 한다.
    """

    def __init__(self, X, y):
        # numpy → torch tensor 변환
        # 입력 feature는 float, 라벨은 long (CrossEntropyLoss 규칙)
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        # 데이터 전체 길이
        return len(self.X)

    def __getitem__(self, idx):
        # idx번째 샘플 하나 반환
        # DataLoader가 이걸 모아서 batch로 만들어줌
        return self.X[idx], self.y[idx]


# ===============================
# 2. Model 정의 (신경망)
# ===============================
class MLP(nn.Module):
    """
    nn.Module을 상속받으면:
    - 파라미터 자동 관리
    - train / eval 모드 전환
    - 저장/로드(state_dict) 가능
    """

    def __init__(self, input_dim):
        super().__init__()

        # 간단한 다층 퍼셉트론(MLP)
        self.net = nn.Sequential(
            nn.Linear(input_dim, 32),  # 입력 → 은닉층
            nn.ReLU(),                 # 비선형성
            nn.Linear(32, 2)            # 출력 (클래스 수 = 2)
        )

    def forward(self, x):
        # 입력 x가 들어오면 어떻게 계산할지 정의
        return self.net(x)


# ===============================
# 3. Trainer 정의 (학습 엔진)
# ===============================
class Trainer:
    """
    Trainer는 '과정(process)'을 담당한다.
    - train loop
    - eval loop
    - optimizer / loss 관리
    """

    def __init__(self, model, optimizer, criterion, device="cpu"):
        self.model = model.to(device)
        self.optimizer = optimizer
        self.criterion = criterion
        self.device = device

    def train_epoch(self, loader):
        """
        학습용 epoch 1회
        """
        self.model.train()  # 학습 모드
        total_loss = 0.0

        for x, y in loader:
            # 배치 데이터를 device(cpu/gpu)로 이동
            x = x.to(self.device)
            y = y.to(self.device)

            # 1) forward
            logits = self.model(x)

            # 2) loss 계산
            loss = self.criterion(logits, y)

            # 3) backward
            self.optimizer.zero_grad()  # 이전 gradient 제거
            loss.backward()             # 미분 계산
            self.optimizer.step()        # 파라미터 업데이트

            total_loss += loss.item()

        # epoch 평균 loss 반환
        return total_loss / len(loader)

    def eval_epoch(self, loader):
        """
        평가용 epoch 1회
        """
        self.model.eval()  # 평가 모드
        correct = 0
        total = 0

        # 평가 시에는 gradient 불필요
        with torch.no_grad():
            for x, y in loader:
                x = x.to(self.device)
                y = y.to(self.device)

                logits = self.model(x)
                preds = logits.argmax(dim=1)  # 가장 점수 높은 클래스 선택

                correct += (preds == y).sum().item()
                total += len(y)

        # 정확도 반환
        return correct / total


# ===============================
# 4. main: 실험 실행
# ===============================
def main():
    # ---------------------------
    # 데이터 로드
    # ---------------------------
    df = pd.read_csv("hero_rankup.csv")

    X = df[['STR', 'INT', 'LUCK', 'PER', 'MIGHT']].values
    y = df['rank_up_success'].values

    # ---------------------------
    # Train / Test split
    # ---------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---------------------------
    # Dataset / DataLoader
    # ---------------------------
    train_ds = HeroDataset(X_train, y_train)
    test_ds  = HeroDataset(X_test, y_test)

    train_loader = DataLoader(
        train_ds,
        batch_size=32,
        shuffle=True
    )

    test_loader = DataLoader(
        test_ds,
        batch_size=32,
        shuffle=False
    )

    # ---------------------------
    # Model / Optimizer / Loss
    # ---------------------------
    model = MLP(input_dim=5)

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=1e-3
    )

    # 분류 문제에서 가장 기본적인 loss
    criterion = nn.CrossEntropyLoss()

    trainer = Trainer(
        model=model,
        optimizer=optimizer,
        criterion=criterion,
        device="cpu"  # GPU 쓰면 "cuda"
    )

    # ---------------------------
    # Training loop
    # ---------------------------
    epochs = 10

    for epoch in range(epochs):
        train_loss = trainer.train_epoch(train_loader)
        test_acc   = trainer.eval_epoch(test_loader)

        print(
            f"[Epoch {epoch+1:02d}] "
            f"train_loss={train_loss:.4f} | "
            f"test_acc={test_acc:.4f}"
        )


# ===============================
# 5. Entry point
# ===============================
if __name__ == "__main__":
    main()
