# SVM
import numpy as np
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

iris = datasets.load_iris()
x = iris['data'][:, (2, 3)]  # 꽃잎 길이와 너비
y = (iris['target'] == 2).astype('int')

svm_clf = Pipeline([
    ('scaler', StandardScaler()),
    ('linear_svc', LinearSVC(C=1, loss='hinge'))
])

# 모델 훈련
svm_clf.fit(x, y)

# 예측
new_iris = [[5.5, 1.7]]  # 길이: 5.5cm, 너비: 1.7
prediction = svm_clf.predict(new_iris)[0]
print(prediction)  # 버지니카!
