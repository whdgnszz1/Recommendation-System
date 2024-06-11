import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# 데이터 생성
x = 2 * np.random.rand(100, 1)  # 0 ~ 2 사이의 균일분포 => shape : 100 x 1
y = 4 + 7 * x + np.random.randn(100, 1)  # y = 4 + 7x + noise, noise는 정규 분포에서 추출된 값

# 이상치 추가
upper_outliers_x_indices = [10, 25, 40]
lower_outliers_x_indices = [60, 80]

# 상단 이상치 추가 (선형 회귀선에서 더 크게 떨어지도록 조정)
for idx in upper_outliers_x_indices:
    y[idx] += 18  # y 값에 상단 이상치 크게 추가

# 하단 이상치 추가 (선형 회귀선에서 더 크게 떨어지도록 조정)
for idx in lower_outliers_x_indices:
    y[idx] -= 18  # y 값에 하단 이상치 크게 추가

# 원래 데이터와 이상치를 함께 시각화
plt.scatter(x, y, c='b', label='Data')
plt.title("Data with Outliers")
plt.legend()
plt.show()

# 선형 회귀 모델을 사용하여 데이터에 맞춤
x_b = np.c_[np.ones((100, 1)), x]  # x에 편향 항 추가
theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)  # 최적의 theta 계산

# 새로운 입력 데이터 정의
x_new = np.array([[0], [2]])
x_new_b = np.c_[np.ones((2, 1)), x_new]

# 새로운 데이터에 대한 예측 값 계산
prediction = x_new_b.dot(theta_best)
print("Predictions using normal equation:", prediction)

# 원래 데이터와 회귀선을 함께 시각화
plt.plot(x_new, prediction, "r-", label="Prediction (normal equation)")
plt.scatter(x, y, c='b', label="Data")
plt.axis([0, 2, 0, 60])
plt.title("Linear Regression with Outliers")
plt.legend()
plt.show()

# 사이킷런 LinearRegression 사용하여 모델 학습 및 예측
lin_reg = LinearRegression()
lin_reg.fit(x, y)
print("Intercept and coefficients using LinearRegression:")
print(lin_reg.intercept_, lin_reg.coef_)

# 새로운 데이터에 대한 예측 값 계산
prediction_sklearn = lin_reg.predict(x_new)
print("Predictions using LinearRegression:", prediction_sklearn)

# 원래 데이터와 회귀선을 함께 시각화 (사이킷런 모델)
plt.plot(x_new, prediction_sklearn, "r-", label="Prediction (sklearn)")
plt.scatter(x, y, c='b', label="Data")
plt.axis([0, 2, 0, 60])
plt.title("Linear Regression with Outliers (sklearn)")
plt.legend()
plt.show()
