#-*- coding: utf-8 -*-
#-*- coding: cp950 -*-

# 工具載入
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#-----.-----.-----.-----.-----.

def printx(string, obj) :
    print "\n" + string + " \n" + str(obj)
#printx("",)

#-----.-----.-----.-----.-----.

alist = [[1,2],[3,4]]
#print alist[1][1]

arr = np.array(alist)
#print arr[1,1]

printx("arr",arr)
printx("arr[0,:]",arr[1,:])
printx("arr[:,0]",arr[:,1])

#-----.-----.-----.-----.-----.
arr = np.arange(3,10)
printx("np.arange(3,10)",arr)

index = np.where(arr > 5) #取得指標 位置
printx("np.where(arr > 5)",index)

new_arr = arr[index] #取得那些值
printx("arr[index]",new_arr)

new_arr = np.delete(arr, index)
printx("np.delete(arr, index)",new_arr)

#-----.-----.-----.-----.-----.
index = arr > 5
printx("arr > 5",index) #相同？
printx("arr > 5",(index)) #相同？
printx("arr[index]",arr[index])


