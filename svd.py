#-*- coding=utf-8 -*-
'''
2017.10.13
奇异值分解
Author:george
'''
import numpy as np
#以下证明公式A=U∑V-1
x = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
a,b,c = np.linalg.svd(x)
print a,b,c
print a*np.diag(b)*c
#以下证明公式
#[A]T A的转置
#[A]TA=V[∑]T[U]TU∑[V]T = V∑2[V]T
print x.transpose()*x
d,e,f = np.linalg.svd(x.transpose()*x)
print d,e,f
print d*np.diag(e)*f
print c.transpose()*np.diag(b**2)*c
