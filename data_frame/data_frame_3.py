import os
import pandas as pd
import numpy as np

base_src = '../machine_learning_data'
# friend.csv 파일 src 변수 할당
abalone_src = os.path.join(base_src, 'abalone.data')

# pandas의 read_csv => 데이터 불러오기
abalone_df = pd.read_csv(abalone_src, header=None, sep=",",
                         names=['sex', 'length', 'diameter', 'height',
                                'whole_weight', 'shucked_weight', 'viscera_weight',
                                'shell_weight', 'rings'],
                         encoding='utf-8')

# 데이터 shape를 확인
# 딥러닝(CNN) => 이미지 (데이터수, 가로, 세로, 채널)
# 딥러닝(RNN) => 텍스트, 시계열 (데이터수, 가로, 세로)
# print(abalone_df.shape)

# 데이터 결측값 확인
# print(abalone_df.isnull().sum().sum())

# 기술통계 확인
# print(abalone_df.describe())

# 전복(abalone) 성별에 따라 groupby 함수를 통해 집계
# mean은 이상치도 반영하기 때문에 이상치를 제외해야 한다.
# grouped = abalone_df['whole_weight'].groupby(abalone_df['sex'])
# print(grouped.sum())
# print(grouped.mean())
# print(grouped.size())

# 그룹 변수가 아닌, 전체 연속형 변수에 대한 집계
# print(abalone_df.groupby(abalone_df['sex']).mean())

# 다음과 같이 간단하게 표현
# print(abalone_df.groupby('sex').mean())

# 새로운 조건에 맞는 변수 추가
abalone_df['length_bool'] = np.where(abalone_df['length'] > abalone_df['length'].median(),
                                     'length_long',
                                     'length_short')

print(abalone_df)

# 그룹 변수를 2개 이상 선택해서 총계 처리?
# EDA
print(abalone_df.groupby(['sex', 'length_bool']).mean())