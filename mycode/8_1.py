# -*- coding:utf-8 -*-
"""
@project = 0524-2
@file = 8_1
@author = Liangjisheng
@create_time = 2018/5/24 0024 下午 19:19
"""
from functools import partial
from matplotlib import pyplot as plt

def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def square(x):
    return x * x

def derivative(x):
    return 2 * x

derivative_estimate = partial(difference_quotient, square, h=0.00001)

# 画出f(x) = x * x函数的导数
x = range(-10, 10)
plt.title('精确的导数值与估计值')
plt.plot(x, list(map(derivative, x)), 'rx', label='Actual')   # 用x来表示
plt.plot(x, list(map(derivative_estimate, x)), 'b+', label='Estimate')    # 用+来表示
plt.legend(loc=9)
plt.show()
