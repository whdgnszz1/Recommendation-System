import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# 파일 경로 설정
base_src = '../machine_learning_data'
u_user_src = os.path.join(base_src, 'u.user')
u_data_src = os.path.join(base_src, 'u.data')
u_item_src = os.path.join(base_src, 'u.item')

# 사용자 데이터 로드
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv(u_user_src, sep='|', names=u_cols, encoding='latin-1')

# 평점 데이터 로드
r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(u_data_src, sep='\t', names=r_cols, encoding='latin-1')

# 영화 데이터 로드
i_cols = ['movie_id', 'title', 'release date', 'video release date', 'IMDB URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
          'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies = pd.read_csv(u_item_src, sep='|', names=i_cols, encoding='latin-1')

# timestamp 제거
ratings = ratings.drop('timestamp', axis=1)
movies = movies[['movie_id', 'title']]

# 데이터 train, test set 분리
x = ratings.copy()
y = ratings['user_id']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, stratify=y)


# 정확도(RMSE)를 계산하는 함수
def RMSE(y_true, y_pred):
    return np.sqrt(np.mean((np.array(y_true) - np.array(y_pred)) ** 2))


# 모델별 RMSE를 계산하는 함수
def score(model):
    id_pairs = zip(x_test['user_id'], x_test['movie_id'])
    y_pred = np.array([model(user, movie) for (user, movie) in id_pairs])
    y_true = np.array(x_test['rating'])
    return RMSE(y_true, y_pred)


# best_seller 함수를 이용한 정확도 계산
train_mean = x_train.groupby(['movie_id'])['rating'].mean()


def best_seller(user_id, movie_id):
    try:
        rating = train_mean[movie_id]
    except KeyError:
        rating = 3.0
    return rating


print(score(best_seller))
