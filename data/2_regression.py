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
X = df[["STR", "INT", "LUCK", "PER", "MIGHT"]].values
y = df[["possibility"]].values


# 훈련용, 테스트용으로 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size= 0.2,
    random_state= 42
)

'''
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
'''  

# 리니어 모델 생성
# 이니셜 가중치와 편향
init_w = np.random.randint(0,1,range(6))
init_b = 0.0
def linear_regression(X, y):
    # forward
    z = X @ init_w + init_b
    
    # 손실 계산

    # 손실 미분 

    # backward(업데이트)
