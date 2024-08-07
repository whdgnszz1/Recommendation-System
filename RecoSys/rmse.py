# 100K의 영화 평점에 대해서 실제값과 best-seller 방식으로 구한 예측값의 RMSE
import os
import pandas as pd
import numpy as np

base_src = '../machine_learning_data'
u_data_src = os.path.join(base_src, 'u.data')
r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(u_data_src,
                      sep='\t',
                      names=r_cols,
                      encoding='latin-1')
ratings = ratings.set_index('user_id')


def RMSE(y_true, y_pred):
    return np.sqrt(np.mean((np.array(y_true) - np.array(y_pred)) ** 2))


# 정확도 계산
rmse = []
movie_mean = ratings.groupby(['movie_id'])['rating'].mean()

for user in set(ratings.index):
    y_true = ratings.loc[user]['rating']
    # best-seller 방식으로
    y_pred = movie_mean[ratings.loc[user]['movie_id']]
    accuracy = RMSE(y_true, y_pred)
    rmse.append(accuracy)

# RMSE 계산
print(np.mean(rmse))
