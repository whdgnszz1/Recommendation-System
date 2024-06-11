import numpy as np
from sklearn.base import clone
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 데이터 생성
data_num = 100
# x 값을 -1에서 2 사이의 랜덤 값으로 생성
x = 3 * np.random.rand(data_num, 1) - 1
# y 값을 0.2 * x^2 + 랜덤 잡음으로 생성
y = 0.2 * (x ** 2) + np.random.randn(data_num, 1)

# 파이프라인 설정: 다항식 변환 및 표준화
poly_scaler = Pipeline([
    ("poly_features", PolynomialFeatures(degree=90, include_bias=False)),
    ('std_scaler', StandardScaler())
])

# 데이터 분할: 80% 학습, 20% 검증
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

# 학습 데이터 변환: 다항식 변환 후 표준화
x_train_poly_scaled = poly_scaler.fit_transform(x_train)
# 검증 데이터 변환: 동일한 변환 적용
x_val_poly_scaled = poly_scaler.transform(x_val)

# SGDRegressor 설정
# warm_start=True: fit 메서드가 호출될 때 처음부터 다시 하지 않고 이전 모델 파라미터에서 훈련 이어짐
# penalty=None: 규제를 사용하지 않음
# max_iter=1: 각 fit 호출에서 1번의 에포크 동안만 학습
# tol=None: 학습이 중지되지 않도록 설정
# learning_rate='constant': 학습률을 일정하게 유지
# eta0=0.0005: 학습률 초기값
sgd_reg = SGDRegressor(max_iter=1, tol=None, warm_start=True, penalty=None,
                       learning_rate='constant', eta0=0.0005, random_state=42)

# 초기 최소 검증 오류 값을 무한대로 설정
minimum_val_error = float('inf')
# 가장 좋은 에포크와 모델을 저장할 변수 초기화
best_epoch = None
best_model = None

no_improvement_count = 0
n_iter_no_change = 10  # 개선이 없을 때 중지하는 에포크 수

# 모델 학습
# 1000번의 에포크 동안 학습
for epoch in range(1000):
    # 학습 데이터를 사용하여 모델 학습
    sgd_reg.fit(x_train_poly_scaled, y_train.ravel())
    # 검증 데이터를 사용하여 예측 수행
    y_val_predict = sgd_reg.predict(x_val_poly_scaled)
    # 검증 오류 계산 (평균 제곱 오차)
    val_error = mean_squared_error(y_val, y_val_predict)
    # 검증 오류가 현재까지의 최소 오류보다 작으면
    if val_error < minimum_val_error:
        # 최소 검증 오류 업데이트
        minimum_val_error = val_error
        # 가장 좋은 에포크 업데이트
        best_epoch = epoch
        # 가장 좋은 모델 클론하여 저장
        best_model = clone(sgd_reg)
        no_improvement_count = 0  # 개선이 있으면 카운트 리셋
    else:
        no_improvement_count += 1  # 개선이 없으면 카운트 증가

    # 개선이 없을 때 학습 중지
    if no_improvement_count >= n_iter_no_change:
        print(f'조기 종료: {epoch} 에포크에서 개선이 없어 학습을 중지합니다.')
        break

# 가장 좋은 에포크와 모델 출력
print('best_epoch : ', best_epoch)
print('best_model : ', best_model)
