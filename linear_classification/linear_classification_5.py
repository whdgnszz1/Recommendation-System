import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

x, y = make_moons(n_samples=1000, noise=0.1, random_state=2024)

# SVM 다항식 커널
# kernel='poly(degree=3)'사용
# 매개변수 coef0는 모델이 높은 차수와 낮은 차수에 얼마나 영향을 받을지 조절하는 것
# coef0을 적절한 값으로 지정하면 고차항의 영향을 줄일 수 있다. (coef0의 default=0)
poly_kernel_std_svm = Pipeline([
    ("std", StandardScaler()),
    ("poly_kernel_svm", SVC(kernel='poly', degree=3, coef0=1, C=5))
])
poly_kernel_std_svm.fit(x, y)

# SVM 가우시안 RBF 커널
# 하이퍼파라미터 r는 규제 역할을 한다.
# (모델이 과적합일 경우=> r 감소시키고, 모델 과소적합일 경우=> r 증가시켜야함)
# 하이퍼파라미터 C도 r(gamma)와 비슷한 성격을 띈다.
# 그래서 모델 복잡도를 조절하기 위해서 gamma와 C를 함께 조절해야 한다.
# Tip (하이퍼파라미터 조절) : 그리드 탐색법 사용(그리드 큰 폭 => 그리드 작은 폭) : 줄여가면서 탐색
rbf_kernel_std_svm = Pipeline([
    ('std', StandardScaler()),
    ('rbf_kernel_svm', SVC(kernel='rbf', gamma=3, C=0.001))
])
rbf_kernel_std_svm.fit(x, y)
