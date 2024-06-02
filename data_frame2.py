import os
import pandas as pd

base_src = 'machine_learning_data'
# friend.csv 파일 src 변수 할당
friend_src = os.path.join(base_src, 'friend.csv')

# pandas의 read_csv => 데이터 불러오기
df = pd.read_csv(friend_src, encoding='utf-8')

# 조건 필터링 가져오기
# 30대 이상만 가져오기
# print(df[df['age'] >= 30])

# job이 intern인 사람 가져오기
# print(df[df['job'] == 'intern'])

# 조건 여러개: DataFrame 안에 괄호로 묶어줘야 한다.
# 30대 이상, 40대 이하
# print(df[(df['age'] >= 30) & (df['age'] <= 40)])

# 조건 여러개 30대 미만 혹은 40대 초과
# print(df[(df['age'] < 30) | (df['age'] > 40)])

# in을 통한 포함 조건 걸기
# print(4 in [1, 3, 5, 8, 23, 515])
# print(df[df['job'].apply(lambda x: x in ['student', 'manager'])])
