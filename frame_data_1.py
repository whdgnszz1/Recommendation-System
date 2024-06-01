import os
import pandas as pd

# Adjust the path based on your current directory structure
base_src = 'machine_learning_data'
# friend.csv 파일 src 변수 할당
friend_src = os.path.join(base_src, 'friend.csv')

# pandas의 read_csv => 데이터 불러오기
df = pd.read_csv(friend_src, encoding='utf-8')

# head() 데이터를 읽어보기 => 5개만 읽기
# print(df.head(6))

new_friend_src = os.path.join(base_src, 'new_friend.csv')
# index=False는 꼭꼭
df.to_csv(new_friend_src, index=False, encoding='utf-8')

# new_friend_src = os.path.join(base_src, 'new_friend_index_true.csv')
# df.to_csv(new_friend_src, index=True, encoding='utf-8')

# 데이터 프레임(집합) => 시리즈 (단일) => 데이터 프레임이 될 수 있겠구나
# series = df['name']
# print(series)


