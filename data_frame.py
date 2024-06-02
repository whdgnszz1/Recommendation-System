import os
import pandas as pd
import numpy as np

base_src = 'machine_learning_data'
# friend.csv 파일 src 변수 할당
friend_src = os.path.join(base_src, 'friend.csv')

# pandas의 read_csv => 데이터 불러오기
df = pd.read_csv(friend_src, encoding='utf-8')

# index 2번에 해당하는 row 가져오기
# print(df.iloc[[4]])

# column 가져오기
# iloc는 숫자형으로 가져온다. 인덱스 위주로
# loc는 문자로 가져오기 정확하게는 DataFrame에 있는 형태 그대로를 가져온다.
# ':' 는 전체를 의미한다. slice 개념 왼쪽은 row, 오른쪽은 column
# print(df['job'])
# print(df.iloc[:, 2])
# print(df.loc[:, 'job'])
#
# print(df.iloc[1, 2])  # 중요!!!! x 1000
# print(df.loc[1, 'job'])  # 중요!!!! x 1000

# row 기준으로, column은 안됨.
# print(df.iloc[2:4])

# column만 하고싶을때는 다음과 같이.
# print(df.iloc[:, :2])

# 문자 => 실수 => 정수

# DataFrame 행, 열, 삭제
# 머신러닝 => 차원의 저주 ......, prune... 가지치기.. 대체값!!...
# 비어있는 값: 통계학 관점에서 대체값 처리가 정말로 중요하다.
# 1. 평균 또는 최빈값
# 2. row 전체를 삭제
# 3. age에 대해 분포를 확률적으로 랜덤 샘플링
# 어떤걸 해야 분포를 알 수 있을까?? => 시각화 (EDA)
# 차원이 너무 많아지면 gradient vanishing 효과가 나타난다. 데이터 과적합이 일어나서 차원을 축소한다.

df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['A', 'B', 'C', 'D'])
# axis=1은 세로방향이다. axis=0은 가로방향 // axis의 기본값은 0이다.
# df.drop(['B','C'], axis=1, inplace=True)
# print(df.drop([0,1], axis=0))
# print(df)
df.loc[1, 'C'] = "육"
print(df)

df.iloc[1, 2] = 6
print(df)

# 슬라이싱 기능을 활용하여 원하는 범위를 바꿀수도 있다.
df.iloc[:, 1] = "끝"
print(df)

df.iloc[:, :] = "끝"
print(df)
