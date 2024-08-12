import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity

base_src = '../machine_learning_data'
u_user_src = os.path.join(base_src, 'u.user')
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv(u_user_src,
                    sep='|',
                    names=u_cols,
                    encoding='latin-1')
users = users.set_index('user_id')

base_src = '../machine_learning_data'
u_data_src = os.path.join(base_src, 'u.data')
r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(u_data_src,
                      sep='\t',
                      names=r_cols,
                      encoding='latin-1')

base_src = '../machine_learning_data'
u_item_src = os.path.join(base_src, 'u.item')
i_cols = ['movie_id', 'title', 'release date', 'video release date',
          'IMDB URL', 'unknown', 'Action', 'Adventure', 'Animation',
          'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
          'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies = pd.read_csv(u_item_src,
                     sep='|',
                     names=i_cols,
                     encoding='latin-1')
movies = movies.set_index('movie_id')


# RMSE 함수
def RMSE(y_true, y_pred):
    return np.sqrt(np.mean((np.array(y_true) - np.array(y_pred)) ** 2))


# 모델별 RMSE를 계산하는 함수: 주어진 모델로 테스트 데이터의 RMSE를 계산합니다.
def score(model):
    # 테스트 데이터의 user_id와 movie_id간 pair를 맞춰 튜플원소 리스트데이터를 만듦
    id_pairs = zip(x_test['user_id'], x_test['movie_id'])
    # 모든 사용자-영화 짝에 대해서 주어진 예측모델에 의해 예측값 계산 및 리스트형 데이터 생성
    y_pred = np.array([model(user, movie) for (user, movie) in id_pairs])
    # 실제 평점값
    y_true = np.array(x_test['rating'])
    return RMSE(y_true, y_pred)


##### 데이터 셋 만들기 #####
x = ratings.copy()
y = ratings['user_id']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, stratify=y)

ratings_matrix = x_train.pivot(index='user_id', columns='movie_id', values='rating')

##### 코사인 유사도 계산 #####
matrix_dummy = ratings_matrix.copy().fillna(0)
user_similarity = cosine_similarity(matrix_dummy, matrix_dummy)
user_similarity = pd.DataFrame(user_similarity,
                               index=ratings_matrix.index,
                               columns=ratings_matrix.index)


##### 주어진 영화의(movie_id) 가중평균 rating을 계산하는 함수 #####
def CF_simple(user_id, movie_id):
    if movie_id in ratings_matrix.columns:
        sim_scores = user_similarity[user_id].copy()
        movie_ratings = ratings_matrix[movie_id].copy()
        none_rating_idx = movie_ratings[movie_ratings.isnull()].index
        movie_ratings = movie_ratings.dropna()
        sim_scores = sim_scores.drop(none_rating_idx)
        mean_rating = np.dot(sim_scores, movie_ratings) / sim_scores.sum()
    else:
        mean_rating = 3.0
    return mean_rating


##### 정확도 계산 #####
print(score(CF_simple))
