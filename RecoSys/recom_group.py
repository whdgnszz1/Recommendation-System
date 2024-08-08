import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# 파일 경로 설정: 데이터 파일들이 저장된 기본 경로를 설정
base_src = '../machine_learning_data'
u_user_src = os.path.join(base_src, 'u.user')  # 사용자 데이터 파일 경로
u_data_src = os.path.join(base_src, 'u.data')  # 평점 데이터 파일 경로
u_item_src = os.path.join(base_src, 'u.item')  # 영화 데이터 파일 경로

# 사용자 데이터 로드: 사용자의 정보가 저장된 데이터
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv(u_user_src, sep='|', names=u_cols, encoding='latin-1')

# 평점 데이터 로드: 사용자가 영화에 매긴 평점 데이터
r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(u_data_src, sep='\t', names=r_cols, encoding='latin-1')

# 영화 데이터 로드: 영화의 메타데이터
i_cols = ['movie_id', 'title', 'release date', 'video release date', 'IMDB URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
          'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies = pd.read_csv(u_item_src, sep='|', names=i_cols, encoding='latin-1')

# timestamp 제거: 평점 데이터에서 timestamp 열을 제거.
ratings = ratings.drop('timestamp', axis=1)

# 영화 데이터에서 movie_id와 title만 선택하여 사용
movies = movies[['movie_id', 'title']]

# 데이터 train, test set 분리
x = ratings.copy()  # 독립 변수
y = ratings['user_id']  # 종속 변수 (사용자 ID)

# 데이터를 75:25 비율로 나누고, y를 기준으로 계층적 샘플링을 적용
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, stratify=y)


# RMSE를 계산하는 함수: 예측값과 실제값의 차이를 계산하여 RMSE를 반환
def RMSE(y_true, y_pred):
    return np.sqrt(np.mean((np.array(y_true) - np.array(y_pred)) ** 2))


# 모델별 RMSE를 계산하는 함수: 주어진 모델로 테스트 데이터의 RMSE를 계산합니다.
def score(model):
    id_pairs = zip(x_test['user_id'], x_test['movie_id'])
    y_pred = np.array([model(user, movie) for (user, movie) in id_pairs])
    y_true = np.array(x_test['rating'])
    return RMSE(y_true, y_pred)


# best_seller 함수를 이용한 정확도 계산
# 영화별 평균 평점을 계산하여 train_mean에 저장
train_mean = x_train.groupby(['movie_id'])['rating'].mean()


# 베스트셀러 모델: 영화의 평균 평점을 반환하는 함수
def best_seller(user_id, movie_id):
    try:
        rating = train_mean[movie_id]  # 해당 영화의 평균 평점
    except KeyError:
        rating = 3.0  # 영화가 없다면 기본값으로 3.0을 반환
    return rating


# 성별에 따른 예측값 계산
# x_train과 users 데이터를 합쳐서 성별에 따른 영화별 평점을 계산
merged_ratings = pd.merge(x_train, users)

users = users.set_index('user_id')

# movie_id와 성별(sex)로 그룹화하여 각 그룹의 평균 평점을 계산
g_mean = merged_ratings[['movie_id', 'sex', 'rating']].groupby(['movie_id', 'sex'])['rating'].mean()

# 평점 데이터를 행: user_id, 열: movie_id로 하는 매트릭스
rating_matrix = x_train.pivot(index='user_id',
                              columns='movie_id',
                              values='rating')

# 성별 기준 협업 필터링 추천 모델
def cf_gender(user_id, movie_id):
    if movie_id in rating_matrix.columns:  # 영화가 rating_matrix에 존재할 경우
        gender = users.loc[user_id]['sex']
        if gender in g_mean[movie_id].index:  # 해당 성별의 평균 평점이 존재할 경우
            gender_rating = g_mean[movie_id][gender]
        else:
            gender_rating = 3.0  # 성별 정보가 없으면 기본값 3.0을 반환
    else:
        gender_rating = 3.0  # 영화가 없으면 기본값 3.0을 반환
    return gender_rating

# 성별 기반 추천 모델의 RMSE를 출력
print(score(cf_gender))
