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

base_src = '../machine_learning_data'
u_data_src = os.path.join(base_src, 'u.data')
r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(u_data_src,
                      sep='\t',
                      names=r_cols,
                      encoding='latin-1')


# RMSE 함수
def RMSE(y_true, y_pred):
    return np.sqrt(np.mean((np.array(y_true) - np.array(y_pred)) ** 2))


def score(model, neighbor_size=0):
    # 테스트 데이터의 user_id와 movie_id간 pair를 맞춰 튜블형원소 리스트데이터를 만듦
    id_pairs = zip(x_test['user_id'], x_test['movie_id'])
    # 모든 사용자-영화 짝에 대해서 주어진 예측모델 의해 예측값 계산 및 리스트형 데이터 생성
    y_pred = np.array([model(user, movie, neighbor_size) for (user, movie) in id_pairs])
    # 실제 평점 값
    y_true = np.array(x_test['rating'])
    return RMSE(y_true, y_pred)


x = ratings.copy()
y = ratings['user_id']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, stratify=y)

ratings_matrix = x_train.pivot(index='user_id', columns='movie_id', values='rating')

##### train set의 모든 가능한 사용자 pair의 cosine similarities 계산 #####
# 코사인 유사도를 구하기 위해 rating값을 복사하고, 계산시 NaN값 에러 대비를 위해 결측치를 0으로 대체
matrix_dummy = ratings_matrix.copy().fillna(0)
# 모든 사용자간 코사인 유사도 구함
user_similarity = cosine_similarity(matrix_dummy, matrix_dummy)
# 필요한 값 조회를 위해 인덱스 및 컬럼명 지정
user_similarity = pd.DataFrame(user_similarity,
                               index=ratings_matrix.index,
                               columns=ratings_matrix.index)

##### 사용자 평가 경향을 고려한 함수 #####
rating_mean = ratings_matrix.mean(axis=1)
rating_bias = (rating_mean.T - rating_mean).T


# 사용자 평가 경향을 고려한 함수
def CF_knn_bias(user_id, movie_id, neighbor_size=0):
    # 영화 ID가 훈련 데이터에 존재하는지 확인
    if movie_id in ratings_matrix.columns:
        sim_scores = user_similarity[user_id].copy()
        movie_ratings = ratings_matrix[movie_id].copy()
        movie_ratings = movie_ratings.dropna()
        sim_scores = sim_scores.drop(movie_ratings.index[movie_ratings.isnull()])

        # 각 사용자의 편향된 평점 적용
        movie_ratings = movie_ratings - rating_mean[movie_ratings.index]

        if neighbor_size == 0:
            # 너무 작은 유사도를 가진 경우를 필터링
            sim_scores = sim_scores[sim_scores > 0]
            if len(sim_scores) > 0:
                prediction = np.dot(sim_scores, movie_ratings) / sim_scores.sum()
                prediction = prediction + rating_mean[user_id]
            else:
                prediction = rating_mean[user_id]
        else:
            if len(sim_scores) > 1:
                neighbor_size = min(neighbor_size, len(sim_scores))
                sim_scores = np.array(sim_scores)
                movie_ratings = np.array(movie_ratings)

                # 유사도 점수를 기반으로 정렬
                user_idx = np.argsort(sim_scores)[-neighbor_size:]

                # user_idx가 movie_ratings의 크기를 넘지 않도록 보장
                user_idx = user_idx[user_idx < len(movie_ratings)]

                sim_scores = sim_scores[user_idx]
                movie_ratings = movie_ratings[user_idx]

                # 너무 작은 유사도를 가진 경우를 필터링
                sim_scores = sim_scores[sim_scores > 0]
                if len(sim_scores) > 0 and len(movie_ratings) > 0:
                    prediction = np.dot(sim_scores, movie_ratings) / sim_scores.sum()
                    prediction = prediction + rating_mean[user_id]
                else:
                    prediction = rating_mean[user_id]
            else:
                prediction = rating_mean[user_id]
    else:
        prediction = rating_mean[user_id]

    return prediction

print(score(CF_knn_bias, 10))
