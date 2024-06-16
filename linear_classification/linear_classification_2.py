from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# iris 데이터셋 로드
iris = datasets.load_iris()

# 꽃잎의 길이와 너비 변수만 사용
x = iris['data'][:, (2, 3)]
y = iris['target']  # 3개 클래스 모두 사용

# 다중 클래스 로지스틱 회귀 모델 생성
# multi_class='multinomial': 소프트맥스 회귀를 사용
# solver='lbfgs': L-BFGS 알고리즘 사용
# C=10: 규제 강도 설정 (L2 규제 사용)
softmax_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', C=10, random_state=2024)
softmax_reg.fit(x, y)

# 새로운 iris 데이터 예측 (꽃잎 길이 5cm, 너비 2cm)
new_iris = [[5, 2]]
prediction = softmax_reg.predict(new_iris)[0]  # 예측된 클래스 라벨
label = iris['target_names'].tolist()  # 클래스 라벨 목록

# 예측된 클래스의 이름 출력
print(label[prediction])

# 예측된 각 클래스에 대한 확률 출력
print(softmax_reg.predict_proba(new_iris))
