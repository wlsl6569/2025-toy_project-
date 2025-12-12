'''
기본적인 Decision Tree에 대해 정리해보자. 의사결정나무(Decision Tree)는 말 그대로 데이터를 가지고
질문을 하나씩 던지면서 분기해 나가는 방식의 모델이다.

트리는 어떤 특징(feature)을 기준으로 데이터를 두 그룹으로 나누는데, 이때 사람이 직접 조건을 만드는 게 아니라
모델이 스스로 “가장 깔끔하게 나눠지는 조건”을 골라서 분기를 만든다.
예를 들어 LUCK이나 STR 같은 값을 기준으로 “LUCK이 57보다 큰가?” 같은 질문을 먼저 던지고,
그 답이 Yes/No인지에 따라 데이터가 둘로 나뉜다. 그 다음에는 각 그룹 안에서 또다시 불순도를 가장 많이 줄이는 기준을 찾아
비슷한 방식으로 한 단계 더 분기한다.
이 분기를 계속 반복하다 보면 마지막에는 모두가 어느 정도 비슷한 성질을 가진 데이터들만 남게 되고,
그 leaf 노드에서 최종적으로 예측값(분류: 성공/실패) 을 결정하게 된다.

트리는 깊어질수록 훈련 데이터는 정말 잘 맞추지만 너무 깊으면 오히려 새로운 데이터에는 성능이 떨어질 수 있기 때문에
보통 max_depth 같은 하이퍼파라미터로 깊이를 적당히 제한해준다.
'''

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv('hero_rankup.csv')
X = df[['STR','INT','LUCK','PER','MIGHT']].values
y = df['rank_up_success'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

clf = DecisionTreeClassifier(random_state=0)


scores = cross_val_score(clf, X_train, y_train, cv=10) # cv 는 cross validation folds 갯수를 의미

print("각 폴드 점수:", scores)   
print("평균 정확도:", scores.mean())
print("표준편차:", scores.std())
