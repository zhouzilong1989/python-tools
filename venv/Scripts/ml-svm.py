#coding=utf-8
#导入svm和数据集
from sklearn import svm,datasets
#调用SVC()
clf = svm.SVC()
#载入鸢尾花数据集
iris = datasets.load_iris()
print "数据集的大小"
print iris.items().__sizeof__()
print iris.data
print iris.target
X = iris.data
y = iris.target
#fit()训练
clf.fit(X,y)
#predict()预测
pre_y = clf.predict(X[5:10])
print "result 1"
print "input"
print X[5:10]
print "output"
print(pre_y)
print(y[5:10])
#导入numpy
import numpy as np
test = np.array([[5.1,2.9,1.8,3.6]])
#对test进行预测
test_y = clf.predict(test)
print(test_y)

X = [[0, 0], [1, 1], [1, 0], [2, 2], [1,-1], [-1,1]]  # training samples
y = [0, 1, 1, 1, 1, 0]  # training target
clf2 = svm.SVC()  # class
clf2.fit(X, y)  # training the svc model
result = clf2.predict([[2, 1],[0.5,-1],[-1,0.5], [0.5, 0.5], [-0.5, -0.5]]) # predict the target of testing samples
print "第二个测试结果"
print result