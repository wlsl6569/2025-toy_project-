'''
Random Forest는 decision tree의 결점(과적합)을 해소해주는 방법으로 decision tree를 여러개 만들어서
데이터를 랜덤하게 뽑고(bootstrap), 특징도 랜덤하게 뽑고(X0값 중 어떤것) 모든 Tree의 결과를 모아 다수결로 결론짓는 classifier나
평균값으로 regression을 할 때 사용하게 된다.

=> 한 나무의 실수값을 다른 나무들이 보정

'''



import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv('hero_rankup.csv')
X = df[['STR','INT','LUCK','PER','MIGHT']].values
y = df['rank_up_success'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)



rf = RandomForestClassifier(
    n_estimators=100,      # 단순 나무 개수, bootstrap아님
    max_depth=None,
    random_state=42, 
    bootstrap = True,  # 어떤 데이터 사용할지 랜덤으로 매번 '복원추출'한다. 한개 데이터를 여러볼 볼 수 있고 어떤 데이터는 아예 안볼 가능성도 있음 : 전체 데이터셋에 대한 과적합 줄이면서도 숲전체적으로 여러번 데이터를 훑는 방법이라 할 수 있겠음.
    max_features='sqrt'  # feature 랜덤성
)

rf.fit(X_train, y_train)
accuracy = rf.score(X_test, y_test)

print("정확도:", accuracy)


