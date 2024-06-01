import os
import pandas as pd

# Adjust the path based on your current directory structure
base_src = 'machine_learning_data'
# friend.csv 파일 src 변수 할당
friend_src = os.path.join(base_src, 'friend.csv')

# pandas의 read_csv => 데이터 불러오기
df = pd.read_csv(friend_src, encoding='utf-8')

# head() 데이터를 읽어보기
print(df.head())
