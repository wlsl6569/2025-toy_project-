'''
Gradient Boosting은 나무들이 순서가 있고 앞 나무의 오답을 뒤 나무가 학습하며 실수를 보정해 나가는 방법이다.

'''
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv('hero_rankup.csv')
X = df[['STR','INT','LUCK','PER','MIGHT']].values
y = df['rank_up_success'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)

from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

gb.fit(X_train, y_train)
print("정확도:", gb.score(X_test, y_test))
