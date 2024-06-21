import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

# 데이터셋 생성: 1000개의 샘플, 노이즈 레벨 0.1, 랜덤 시드 2024
x, y = make_moons(n_samples=1000, noise=0.1, random_state=2024)

# 파이프라인 구성
# 1. 다항식 변환: 3차 다항식 특징 생성
# 2. 표준화: StandardScaler를 사용하여 특징을 표준화
# 3. 선형 SVM 모델: LinearSVC를 사용하여 학습, C=10, 힌지 손실 함수 사용
polynomial_std_svm = Pipeline([
    ("polynomial", PolynomialFeatures(degree=3)),  # 다항식 특징 생성 (3차 다항식)
    ('std', StandardScaler()),  # 표준화 (평균 0, 분산 1)
    ('svm', LinearSVC(C=10, loss='hinge'))  # 선형 SVM 모델, C=10, 힌지 손실 함수 사용
])

# 모델 학습: 파이프라인을 통해 데이터 x와 레이블 y로 학습
polynomial_std_svm.fit(x, y)

# 예측: 새로운 데이터 포인트 [2.0, 1.0]에 대한 예측
new_moon = [[2.0, 1.0]]
print(polynomial_std_svm.predict(new_moon))  # 예측 결과 출력
