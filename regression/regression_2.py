import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# 경사 하강법 구현 (implementation)

x = 2 * np.random.rand(100, 1)  # 100 x 1
x_b = np.c_[np.ones((100, 1)), x]
y = 4 + 3 * np.random.randn(100, 1)

learning_rate = 0.001
iterations = 1000
m = x_b.shape[0]  # x의 데이터 수

theta = np.random.randn(2, 1)

for iteration in range(iterations):
    gradients = 2 / m * x_b.T.dot(x_b.dot(theta) - y)
    theta = theta - (learning_rate * gradients)

print(theta)
