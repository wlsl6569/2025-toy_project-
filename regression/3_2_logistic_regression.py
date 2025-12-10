'''
logistic_regression은 회귀를 이용하여 그 선을 기준으로 들어오는 데이터를 0 또는 1로 분류하는 모델이다.
만든 hero 데이터를 이용하여 rank_up_success를 예측하는 모델을 만들어보자

로지스틱 회귀분류에서는 1차적으로 linear regression으로 z값(이전 선형회귀에선 y_pred값)을 구하여
z를 시그모이드 함수에 넣어 확률값으로 변환한다.이 확률이 임계값을 넘냐 못넘냐로 0 또는 1 로 최종출력값이 결정된다.
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('hero_rankup.csv')
X = df[["STR", "INT", "LUCK", "PER", "MIGHT"]].values # 2차원짜리로 만든다 (300, 5)
y = df['rank_up_success'].values # 1차원배열 (300,)

X_train, X_test, y_train, y_test = train_test_split(X,y)





# 시그모이드 함수 정의
def sigmoid(z):
    p = 1/(1+np.exp(-z))
    return p


# 모델 정의
def logistic_regression(X,y,lr = 0.0001, epochs = 1000):

    # 초기 w, b값 결정
    n_samples, n_features = X.shape
    w = np.random.randn(n_features) # (300,5) @ (5, )가 되어야 함.
    b = 0 

    # 들어오는 데이터 X에서 feature 갯수와 sample 갯수 찾기
    n_samples, n_features = X.shape
    
    for epoch in range(epochs):

        # z값 구하기
        z = X @ w + b 

        # sigmoid 확률분포에 z값 매핑
        p = sigmoid(z)

        # 임계값을 넘는가?
        y_pred = []
        
        for prob in p:
            if prob >= 0.5:
                y_pred.append(1)
            else :
                y_pred.append(0)
        y_pred = np.array(y_pred)   # list를 넘파이 행렬로 바꾸기
        

        # error와 Loss(손실값) 정의
        error_1 = y_pred-y # for MSE
        error_2 = p-y # for BCE
        L_op1 = 1/n_samples*(sum(error_1**2))   # 첫번째 손실함수 옵션 : MSE
        L_op2 = -(1/n_samples) * np.sum(y*np.log(p + 1e-8) + (1-y)*np.log(1 - p + 1e-8)) # 두번째 손실함수 옵션 : BCE, p에 아주작은 수를 더한 이유는 log(0) => 정의 불가는 이어서

        # dw db 정의
        dw = (2 / n_samples) * (X.T @ error_2)  
        db = (2 / n_samples) * np.sum(error_2)

        # w, b 업데이트
        w -= dw
        b -= db

        # 에포크 수만큼 반복
        if (epoch) % 200 == 0:
            print(f'====== train : {epoch}/{epochs}, loss : {L_op2:.3f} ========')

    
    return w,b

    
w,b = logistic_regression(X_train, y_train, lr = 0.0001, epochs=1000)
print(f'{w}')
print(f'{b:.3f}')


# --------------------------------------------------------------------------------
# test
# --------------------------------------------------------------------------------



def evaluate_logistic(X, y, w, b):
    n_samples, n_features = X.shape

    # z, p
    z = X @ w + b
    p = sigmoid(z)

    # 0/1 예측
    y_pred = (p >= 0.5).astype(int)

    # BCE loss
    loss = -(1/n_samples) * np.sum(
        y * np.log(p + 1e-8) + (1-y) * np.log(1 - p + 1e-8)
    )

    # accuracy
    accuracy = np.mean(y_pred == y)

    return loss, accuracy, p, y_pred


test_loss, test_acc, p_test, y_pred_test = evaluate_logistic(X_test, y_test, w, b)
print(f"Test Loss (BCE): {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")


'''
====== train : 0/1000, loss : 8.089 ========
====== train : 200/1000, loss : 3.212 ========
====== train : 400/1000, loss : 2.411 ========
====== train : 600/1000, loss : 2.057 ========
====== train : 800/1000, loss : 2.357 ========
[-0.11895298  2.70228051  2.92625402  0.37727846 -0.79858933]
-20.263
Test Loss (BCE): 2.2139
Test Accuracy: 0.7467




====== train : 0/1000, loss : 2.356 ========
====== train : 200/1000, loss : 2.855 ========
====== train : 400/1000, loss : 3.194 ========
====== train : 600/1000, loss : 1.625 ========
====== train : 800/1000, loss : 0.816 ========
[2.44096691 3.99707003 3.9302199  2.45796312 1.30183932]
-22.962
Test Loss (BCE): 2.4484
Test Accuracy: 0.8533
->정답은 많이 맞췄지만, 확률값(p)이 대체로 0.5 근처라서 자신감이 낮았음. 그래서 log loss가 크게 나왔다

'''