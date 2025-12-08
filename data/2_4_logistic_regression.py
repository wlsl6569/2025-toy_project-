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




# 모델 정의
def logistic_regression(X,y,lr = 0.0001, epochs = 1000):
    # 들어오는 데이터 X에서 feature 갯수와 sample 갯수 찾기

    # z값 구하기

    # sigmoid 확률분포에 z값 매핑

    # 임계값을 넘는가?

    # error와 Loss(손실값) 정의

    # 에포크 수만큼 반복

    