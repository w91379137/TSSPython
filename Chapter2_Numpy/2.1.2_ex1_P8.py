#-*- coding: utf-8 -*-
#-*- coding: cp950 -*-

# 工具載入
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def printx(string, obj) :
    print "\n" + string + " \n" + str(obj)
#printx("",)

#-----.-----.-----.-----.-----.
recarr = np.zeros((2,), dtype = ('i4,f4,a10'))
toadd = [(1,2.,'Hello'),(2,3.,'World')]
recarr[:] = toadd

printx("recarr",recarr)


#-----.-----.-----.-----.-----.
#這個格式是一定要打出來的 dtype = ('i4,f4,a10')
recarr = np.zeros((2,), dtype = ('i4,f4,a10'))

col1 = np.arange(2) + 1
col2 = np.arange(2, dtype = np.float32)
col3 = ['Hello', 'World']

toadd = zip(col1, col2, col3)
recarr[:] = toadd

recarr.dtype.names = ('Intergers', 'Floats', 'Strings')
printx("recarr['Intergers']",recarr['Intergers'])
printx("recarr['Floats']",recarr['Floats'])
printx("recarr['Strings']",recarr['Strings'])
