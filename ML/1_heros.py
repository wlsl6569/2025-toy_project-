'''
text에 들어갈 데이터를 생성하자
'''

import pandas as pd
import numpy as np

# 값고정
np.random.seed(42)

hero_num = 300

# 영웅들 능력치 조절
hp = np.random.randint(0, 11, size = hero_num)
mp = np.random.randint(0, 11, size = hero_num)
luck = np.random.randint(0, 11, size=hero_num)
personality = np.random.randint(0, 11, size = hero_num)
might = np.random.randint(0,11, size= hero_num) 

# 능력치 0~1로 변환하기 위한 시그모이드 함수
def sigmoid(z):
    return 1/(1+np.exp(-z))     # 리스트를 계산할때 e**(-z)는 단수하나만 계산가능하여 np에서 지수함수 꺼내 사용

# 각 능력별 가중치 계수를 랜덤값으로 잡아놓고 편향 b도 정해주는데 이걸 통해 정답지 만드는거라 후에 모델이 이걸 맞추는 게 우리 목표가 된다. 
true_w = np.array([0.025, 0.4, 0.3, 0.01, 0.01])
true_b = -1.2

# vstack으로 각 능력들 행을 붙여주고 이를 T로 전치해줘서 모양을 ML에 맞게 수정
X = np.vstack([hp, mp, luck, personality, might]).T

# 선형결합 z와 시그모이드 확률 p를 만들어준다
z = X@true_w + true_b 
p = sigmoid(z)


# p를 성공확률로 보고 베르누이 분포에서 0 or 1 샘플링
# np.random.rand()는 0~1 균등분포로 p보다 작으면 성공(1)하게 기록됨
y = (np.random.rand(hero_num) < p).astype(int)

# pandas DataFrame으로 정리
df = pd.DataFrame({
    "STR": hp,
    "INT": mp,
    "LUCK": luck,
    "PER": personality,
    "MIGHT" : might,
    "possibility" : np.round(z, 3),
    "rank_up_success" : y
})

#print(df.head)
df.to_csv('hero_rankup.csv', index = False)