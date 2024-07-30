# 사용자 u.data 파일을 DataFrame으로 읽기
import os
import pandas as pd

base_src = '../machine_learning_data'
u_data_src = os.path.join(base_src, 'u.data')
r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(u_data_src,
                    sep='\t',
                    names=r_cols,
                    encoding='latin-1')
ratings = ratings.set_index('user_id')
print(ratings.head())