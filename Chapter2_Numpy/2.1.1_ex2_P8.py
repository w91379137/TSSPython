#-*- coding: utf-8 -*-
#-*- coding: cp950 -*-

# 工具載入
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def printx(string, obj) :
    print "\n" + string + " \n" + str(obj)
#printx("",)

printx("np.zeros(2, dtype = int)",np.zeros(2, dtype = int))
printx("np.zeros(2, dtype = np.float32)",np.zeros(2, dtype = np.float32))

arr1d = np.arange(8)
printx("np.arange(10)",arr1d)

arr3d = arr1d.reshape((2,2,2))
printx("arr1d.reshape((2,2,2))",arr3d)

#數目不一樣都過不去
arr3d = np.reshape(arr1d, (2,2,2))
printx("np.reshape(arr1d, (2,2,2))",arr3d)

arr1d = np.zeros((2,2,2,2)).ravel()
printx("np.zeros((2,2,2,2))",np.zeros((2,2,2,2)))
printx("np.zeros.((2,2,2,2)).ravel()",arr1d)