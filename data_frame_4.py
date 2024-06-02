import os
import pandas as pd
import numpy as np

base_src = 'machine_learning_data'
# friend.csv 파일 src 변수 할당
abalone_src = os.path.join(base_src, 'abalone.data')

# pandas의 read_csv => 데이터 불러오기
abalone_df = pd.read_csv(abalone_src, header=None, sep=",",
                         names=['sex', 'length', 'diameter', 'height',
                                'whole_weight', 'shucked_weight', 'viscera_weight',
                                'shell_weight', 'rings'],
                         encoding='utf-8')

# 중복 데이터 삭제 결측치 => 중복된 데이터 확인
# 중복된 row를 확인하는 법
# print(abalone_df.duplicated().sum())

# 중복 예제 생성을 위해서, 가상으로 중복데이터 생성
new_abalone = abalone_df.iloc[[0]]
new_abalone_df = pd.concat([abalone_df, new_abalone], axis=0)
# print(new_abalone_df.duplicated().sum())
new_abalone_df.duplicated(keep='last')

# 중복 데이터(row) 삭제
new_abalone_df = new_abalone_df.drop_duplicates()
# print(new_abalone_df.duplicated(keep='last').sum())

# NaN(결측치)를 찾아서 다른 값으로 변경
# 기존 데이터에는 결측치가 존재X
# print(abalone_df.isnull().sum().sum())

nan_abalone_df = abalone_df.copy()
nan_abalone_df.loc[2, 'length'] = np.nan
# print(nan_abalone_df.isnull().sum().sum())

# 결측치를 특정 값으로 채우기
# 실수 > 정수
# zero_abalone_df = nan_abalone_df.fillna(0)
# print(zero_abalone_df)
# print(zero_abalone_df.isnull().sum().sum())

# 결측치를 결측치가 속한 컬럼의 평균값으로 대체하기
print(nan_abalone_df['length'].fillna(nan_abalone_df['length'].mean()))

