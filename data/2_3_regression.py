'''
기본적인 liner regression에 대해 정리해보자.
선형 회귀란 기존데이터를 토대로 직선을 만들어 그 직선이
새로 들어온 데이터의 값을 가장 잘 예측하도록 만드는 것이다.
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


# 만들어둔 데이터 불러오기
df = pd.read_csv('hero_rankup.csv')
#print(df.head())

# 특징값과 정답 따로 분리
X = df[["STR", "INT", "LUCK", "PER", "MIGHT"]].values   # 2차원 특징*개수
y = df["possibility"].values  # 정답 레이블은 1차원으로 불러오기


# 훈련용, 테스트용으로 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size= 0.2,
    random_state= 42
)
'''
print(X_train.shape) #(240, 5)
print(X_test.shape) # (60, 5)
print(y_train.shape) # (240, 1)
print(y_test.shape) # (60, 1)
'''


# 리니어 모델 생성
# 이니셜 가중치와 편향
n_samples = X.shape[1]
init_w = np.random.randint(0,1,size=n_samples)
init_b = 0.0

# 선형 회귀 
def linear_regression(X, y, lr=0.0001, epochs=10):  # lr이 너무 크면 학습 발산 가능
    n_samples, n_features   = X.shape  
    print(f'n_features : {n_features}')  # 5가 나와야함
    print(f'n_samples : {n_samples}')   # 들어온 X의 n만큼 나와야함 
 
    # 초기 가중치, 편향
    w = np.random.randn(n_features)   # (5)
    b = 0.0

    for epoch in range(epochs):
        # forward
        y_pred = X @ w + b            # (nX5) @ (5) + b

        # error & loss
        error = y_pred.T - y            # 여기서 y_pred와 y모양 잘맞추기 애초에 y불러올떄 1차원으로 불러오면 좋은듯
        loss = np.mean(error**2)

        # gradient (dw, db)
        dw = (2 / n_samples) * (X.T @ error)    # (2 / n_samples)에 곱해지는 (X.T @ error)모양은 [(5Xn @ nX5)]
        db = (2 / n_samples) * np.sum(error)    # scalar

        # update
        w -= lr * dw
        b -= lr * db

        # 중간 출력
        if (epoch + 1) % 200 == 0:
            print(f"{epoch+1}/{epochs} epochs, loss={loss:.3f}")

    return w, b


# 5. 학습 돌리기
w_learned, b_learned = linear_regression(X_train, y_train, lr=0.0001, epochs=1000)


print(f"학습된 w: {w_learned}")
print(f"학습된 b: {b_learned:.3f}")


# 6. 정답지 대입

y_pred_test = X_test @ w_learned + b_learned
test_error = y_pred_test - y_test
test_loss = np.mean(test_error ** 2)
print("테스트 손실:", test_loss)

print("=== 테스트 결과 ===")
print("테스트 loss:", test_loss)