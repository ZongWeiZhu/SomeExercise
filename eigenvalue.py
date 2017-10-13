#-*- coding=utf-8 -*-
'''
2017.10.13
矩阵的特征值与特征向量
Author:george
'''
import numpy as np

x = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
values,vectors = np.linalg.eig(x)
print values,vectors
v = vectors[:,0] #获得矩阵的某一列
#X=Q∑Q-1
#print vectors*np.diag(values) * np.linalg.inv(vectors)
#XQ=λQ
print v*values[0]
print x*v


