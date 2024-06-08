import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# 확률적 경사 하강법 구현
x = 2 * np.random.rand(100, 1)  # 100 x 1
x_b = np.c_[np.ones((100, 1)), x]
y = 4 + 3 * np.random.randn(100, 1)

epochs = 1000
t0, t1 = 5, 50  # 학습 스케쥴 (하이퍼 파라미터)
m = x_b.shape[0]


def learning_schedule(t):
    return t0 / (t + t1)


theta = np.random.randn(2, 1)  # 2 x 1 크기의 평균 0, 분산 1 정규 분포 추출

for epoch in range(epochs):
    for i in range(m):
        random_index = np.random.randint(m)  # 0 ~ m-1까지 랜덤 숫자 1
        xi = x_b[random_index:random_index + 1]  # 1 x 2 크기
        yi = y[random_index:random_index + 1]  # 1 x 1 크기
        gradients = 2 * xi.T.dot(xi.dot(theta) - yi)  # 1 => mini_m
        learning_rate = learning_schedule(epoch * m + i)
        theta = theta - learning_rate * gradients

print(theta)
