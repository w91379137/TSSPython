#-*- coding: utf-8 -*-
#-*- coding: cp950 -*-

# 工具載入
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def printx(string, obj) :
    print "\n" + string + " \n" + str(obj)

arr = np.array([1,2,3])
printx("np.array([1,2,3])", arr)

arr = np.zeros(5)
printx("np.zeros(5)", arr)

arr = np.arange(5)
printx("np.arange(5)", arr)

arr = np.arange(6,10)
printx("np.arange(6,10)", arr)

arr = np.linspace(0,10,6)
printx("np.linspace(0,10,6)", arr)

#例 : 印出 10^0 ~ 10^1 分100個 np.logspace(0,1,100)
arr = np.logspace(0,8,9, base = 2)
printx("np.logspace(0,8,9, base = 2)", arr)

image = np.zeros((2,3))
printx("np.zeros((2,3))", image)

cube = np.zeros((2,3,4)).astype(int) + 1
printx("np.zeros((2,3,4)).astype(int) + 1", cube)
#http://stackoverflow.com/questions/28010860/slicing-3d-numpy-arrays

cube = np.zeros((2,3,4)).astype(np.float16) + 0.1
printx("np.zeros((2,3,4)).astype(np.float16) + 0.1", cube)
