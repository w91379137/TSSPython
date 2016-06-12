#-*- coding: utf-8 -*-
#-*- coding: cp950 -*-

# 工具載入
import timeit
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

arr = np.arange(1e4)
larr = arr.tolist()

def list_times(alist, scalar) :
    for i, val in enumerate(alist) :
        alist[i] = val * scalar
    return alist

timeit.timeit("A", arr * 1.1)
timeit.timeit("B", list_times(larr, 1.1))


