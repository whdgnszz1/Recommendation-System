import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# x는 0부터 2 사이의 균일분포를 가지는 100개의 샘플을 생성한다.
# np.random.rand(100, 1)는 0과 1 사이의 난수를 가지는 100x1 배열을 생성하고,
# 이 배열에 2를 곱하면 0과 2 사이의 난수를 가지는 100x1 배열이 된다.
x = 2 * np.random.rand(100, 1)  # 0 ~ 2 사이의 균일분포 => shape : 100 x 1

# y는 x에 선형 방정식을 적용하고, 정규 분포를 따르는 잡음을 추가하여 생성한다.
# 4 + 3 * x는 선형 방정식 y = 4 + 3x를 의미한다.
# np.random.randn(100, 1)는 평균이 0이고 분산이 1인 정규 분포에서 샘플링된 100x1 배열을 생성한다.
# 이 값을 y에 더하여 노이즈를 추가한다.
y = 4 + 3 * x + np.random.randn(100, 1)  # y = 4 + 3x + noise, noise는 정규 분포에서 추출된 값

# plt.scatter를 사용하여 x와 y 값을 산점도로 시각화한다.
plt.scatter(x, y)
# plt.show()

# np.c_는 두 배열을 열 단위로 결합한다.
# np.ones((100, 1))는 100x1 배열을 생성하며, 모든 값이 1이다.
# x_bias는 x의 앞에 1로 이루어진 열 벡터를 추가하여 (100, 2) 형태의 배열을 만든다.
# 이는 선형 회귀 모델에서 절편(편향) 항을 추가하기 위한 전처리 과정이다.
x_b = np.c_[np.ones((100, 1)), x]

# 선형 회귀 모델의 매개변수(theta)를 계산한다.
# np.linalg.inv는 주어진 행렬의 역행렬을 계산한다.
# x_b.T.dot(x_b)는 x_b의 전치 행렬과 x_b의 곱을 계산한다.
# (x_b.T.dot(x_b))의 역행렬에 x_b.T를 곱하고, 다시 y를 곱하여 최적의 theta 값을 구한다.
theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)
# print(theta_best)

# 새로운 입력 데이터 x_new를 정의한다.
x_new = np.array([[0], [2]])
x_new_b = np.c_[np.ones((2, 1)), x_new]

# 새로운 데이터에 대한 예측 값을 계산한다.
prediction = x_new_b.dot(theta_best)
print(prediction)

# 원래 데이터와 회귀선을 함께 플롯한다.
plt.plot(x_new, prediction, "r-")
plt.plot(x, y, 'b.')
plt.axis([0, 2, 0, 15])
plt.show()

lin_reg = LinearRegression()
lin_reg.fit(x, y)
print(lin_reg.intercept_, lin_reg.coef_)
