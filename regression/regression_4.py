import numpy as np

# 데이터 개수 설정
data_num = 1000

# -1과 2 사이의 값을 가지는 1000개의 난수를 생성
x = 3 * np.random.rand(data_num, 1) - 1

# y 값 생성: 0.2 * x^2 + 정규분포에서 뽑은 랜덤 값
# 여기서 np.random.randn(1000, 1)은 평균이 0이고 표준편차가 1인 정규분포를 따르는 1000개의 랜덤 값을 생성
y = 0.2 * (x ** 2) + np.random.randn(1000, 1)

# PolynomialFeatures를 사용하여 다항 특징 생성
from sklearn.preprocessing import PolynomialFeatures

# degree=2로 설정하여 2차 다항식의 특징을 생성, include_bias=False는 편향 항을 포함하지 않음
poly_features = PolynomialFeatures(degree=2, include_bias=False)

# x 데이터를 2차 다항식 특징으로 변환
x_poly = poly_features.fit_transform(x)

# 변환 전의 첫 번째 x 값 출력
print(x[0])

# 변환 후의 첫 번째 x_poly 값 출력
print(x_poly[0])

# 선형 회귀 모델을 가져옴
from sklearn.linear_model import LinearRegression

# LinearRegression 객체를 생성
lin_reg = LinearRegression()

# 변환된 x_poly와 y를 사용하여 모델을 학습
lin_reg.fit(x_poly, y)

# 학습된 모델의 절편(intercept)과 계수(coef)를 출력 (처음 설정했던 0.2와 비슷한 것을 확인)
print(lin_reg.intercept_, lin_reg.coef_)
