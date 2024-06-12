from sklearn import datasets

# iris 데이터셋 로드
iris = datasets.load_iris()

# 꽃잎의 너비 변수만 사용 (iris 데이터셋의 네 번째 열)
x = iris['data'][:, 3:]  # 꽃잎의 너비 변수만 사용
# 타겟이 'virginica' (index = 2)인 경우를 binary classification의 타겟으로 설정
y = (iris['target'] == 2).astype('int')  # index = 2 : virginica

from sklearn.linear_model import LogisticRegression

# 로지스틱 회귀 모델 초기화
log_reg = LogisticRegression()
# 모델 학습 (꽃잎의 너비 변수 x와 타겟 y를 사용)
log_reg.fit(x, y)

import numpy as np
import matplotlib.pyplot as plot

# 0에서 3까지 1000개의 값을 가진 배열 생성 (새로운 입력 데이터)
x_new = np.linspace(0, 3, 1000).reshape(-1, 1)
# 새로운 입력 데이터에 대한 예측 확률 계산
y_proba = log_reg.predict_proba(x_new)

# 예측 확률 그래프 그리기
plot.plot(x_new, y_proba[:, 0], "b-", label="Not Virginica")  # virginica가 아닐 확률
plot.plot(x_new, y_proba[:, 1], "g-", label="Virginica")      # virginica일 확률
plot.xlabel("Petal width (cm)")  # x축 라벨
plot.ylabel("Probability")  # y축 라벨
plot.legend()  # 범례 표시
plot.show()  # 그래프 출력
