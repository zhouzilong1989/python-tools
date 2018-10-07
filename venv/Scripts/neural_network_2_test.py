#coding:utf-8
#基于NeuralNetwork的XOR（异或）示例
import numpy as np
from neural_network_2 import NeuralNetwork

nn = NeuralNetwork([2,2,1], 'tanh')
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
nn.fit(X, y)
for i in [[0, 0], [0, 1], [1, 0], [1,1]]:
    print(i,nn.predict(i))