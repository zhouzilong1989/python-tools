#coding:utf-8
import numpy as np

#定义双曲函数和他们的导数
def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
    return 1.0 - np.tanh(x)**2

def logistic(x):
    return 1/(1 + np.exp(-x))

def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))

#定义NeuralNetwork 神经网络算法
class NeuralNetwork:
    #初始化，layers表示的是一个list，eg[10,10,3]表示第一层10个神经元，第二层10个神经元，第三层3个神经元
    def __init__(self, layers, activation='tanh'):
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv

        self.weights = []
        #循环从1开始，相当于以第二层为基准，进行权重的初始化
        for i in range(1, len(layers) - 1):
            #对当前神经节点的前驱赋值
            self.weights.append((2*np.random.random((layers[i - 1] + 1, layers[i] + 1))-1)*0.25)
            #对当前神经节点的后继赋值
            self.weights.append((2*np.random.random((layers[i] + 1, layers[i + 1]))-1)*0.25)
            print "初始化权重"
            print self.weights

    #训练函数   ，X矩阵，每行是一个实例 ，y是每个实例对应的结果，learning_rate 学习率，
    # epochs，表示抽样的方法对神经网络进行更新的最大次数
    def fit(self, X, y, learning_rate=0.2, epochs=2):
        X = np.atleast_2d(X) #确定X至少是二维的数据
        temp = np.ones([X.shape[0], X.shape[1]+1]) #初始化矩阵
        temp[:, 0:-1] = X # adding the bias unit to the input layer
        X = temp
        y = np.array(y) #把list转换成array的形式

        for k in range(epochs):
            #随机选取一行，对神经网络进行更新
            print("随机选取一行，对神经网络进行更新")
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            print "随机行为："
            print a

            #完成所有正向的更新
            for l in range(len(self.weights)):
                print "正向更新" + str(l)
                print a[l]
                print self.weights[l]
                a.append(self.activation(np.dot(a[l], self.weights[l])))
                print a
            print "完成所有正向的更新"
            print "随机行变为："
            print a

            error = y[i] - a[-1]
            deltas = [error * self.activation_deriv(a[-1])]

            print "误差error为："
            print error
            print "deltas为："
            print deltas

            #开始反向计算误差，更新权重
            print "开始反向计算误差，更新权重"
            for l in range(len(a) - 2, 0, -1): # we need to begin at the second to last layer
                print "次数为：" + str(l)
                print a[l]
                print self.weights[l]
                print deltas[-1]
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_deriv(a[l]))
            print "deltas变为："
            print deltas
            deltas.reverse()
            print "deltas反转："
            print deltas
            for i in range(len(self.weights)):
                print "更新权重次数：" + str(i)
                print a[i]
                print deltas[i]
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)
                print self.weights[i]
            print "更新后的权重为："
            print self.weights
    #预测函数
    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0]+1)
        temp[0:-1] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a