import os
import pandas as pd
import numpy as np
import math

base_src = '../machine_learning_data'
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
# print(nan_abalone_df['length'].fillna(nan_abalone_df['length'].mean()))

# 꽃..!
# apply함수 !!!!!! 진짜 강추 !!!!!!
# apply함수 활용
# DataFrame타입의 객체에서 호출가능한 apply함에 대해 살펴보자.
# 본인이 원하는 행과 열에 연산 혹은 function을 적용할 수 있다.
# 열 기준으로 집계하고 싶은 경우 axis=0
# 행 기준으로 집계하고 싶은 경우 axis=1

# 열 기준 집계
# print(abalone_df[['diameter']].apply(np.average, axis=0))

# 행 기준 집계
# print(abalone_df[['diameter', 'whole_weight']].apply(np.average, axis=1))

# 사용자 함수를 통한 집계 아주아주아주아주 중요
def avg_ceil(x, y, z):
    return math.ceil((x + y + z))


# 문제
# 1. 사용자 정의 함수 사용
# 2. ['diameter', 'height', 'whole_weight'] 변수 사용
# 3. 세 변수의 합이 1이 넘으면 True, 아니면 False 출력 후 answer 변수에 저장
# 4. abalone_df에 answer 열을 추가하고 입력
# answer = abalone_df[['diameter', 'height', 'whole_weight']].apply(lambda x: avg_ceil(x[0], x[1], x[2]), axis=1) > 1
# abalone_df['answer'] = answer
# print(abalone_df)

# 컬럼 내 유니크한 값 뽑아서 개수 확인 (카테고리 변수)
# print(abalone_df['sex'].value_counts(dropna=True, ascending=True))

# 두 개의 DataFrame 합치기
# 가상 abalone 1개 row데이터 생성 및 결합
one_abalone_df = abalone_df.iloc[[0]]
abalone_df = abalone_df.concat([abalone_df, one_abalone_df], axis=0)
print(abalone_df)
