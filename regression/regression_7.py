import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

import matplotlib.pyplot as plt

# 데이터 개수 설정
data_num = 1000

# -1과 2 사이의 값을 가지는 1000개의 난수를 생성
x = 3 * np.random.rand(data_num, 1) - 1

# y 값 생성: 0.2 * x^2 + 정규분포에서 뽑은 랜덤 값
# 여기서 np.random.randn(1000, 1)은 평균이 0이고 표준편차가 1인 정규분포를 따르는 1000개의 랜덤 값을 생성
y = 0.2 * (x ** 2) + np.random.randn(1000, 1)

# PolynomialFeatures를 사용하여 다항 특징 생성
poly_features = PolynomialFeatures(degree=2, include_bias=False)

# x 데이터를 2차 다항식 특징으로 변환
x_poly = poly_features.fit_transform(x)

# 변환 전의 첫 번째 x 값 출력
print(x[0])

# 변환 후의 첫 번째 x_poly 값 출력
print(x_poly[0])

# 선형 회귀 모델을 가져옴
lin_reg = LinearRegression()

# 변환된 x_poly와 y를 사용하여 모델을 학습
lin_reg.fit(x_poly, y)

# 학습된 모델의 절편(intercept)과 계수(coef)를 출력
print(lin_reg.intercept_, lin_reg.coef_)


# 학습 곡선 그리기 함수 정의
def plot_learning_curves(model, x, y):
    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2)
    train_errors, val_errors = [], []
    for num in range(1, len(x_train)):
        model.fit(x_train[:num], y_train[:num])
        y_train_predict = model.predict(x_train[:num])
        y_val_predict = model.predict(x_val)
        train_errors.append(mean_squared_error(y_train[:num], y_train_predict))
        val_errors.append(mean_squared_error(y_val, y_val_predict))
    plt.plot(np.sqrt(train_errors), 'r-+', linewidth=2, label='train_set')
    plt.plot(np.sqrt(val_errors), 'b-', linewidth=3, label='val_set')
    plt.legend()
    plt.xlabel('Training set size')
    plt.ylabel('RMSE')
    plt.show()


# 학습 곡선 출력
data_num = 100
x = 3 * np.random.rand(data_num, 1) - 1
y = 0.2 + (x ** 2) + np.random.randn(100, 1)
polynomial_regression = Pipeline([
    ("poly_features", PolynomialFeatures(degree=4, include_bias=False)),
    ('lin_reg', LinearRegression())
])
plot_learning_curves(polynomial_regression, x, y)

# Ridge 회귀
# 안드레 루이 숄레스키가 발견한 행렬 분해(Matrix factorization) 사용
# 숄레스키 분해의 장점은 성능이다. 원래 ridge의 solver default 값은 'auto'이며 희소 행렬이다.
ridge_reg = Ridge(alpha=0.1, solver='cholesky')
ridge_reg.fit(x, y)
print(ridge_reg.predict([[1.5]]))
