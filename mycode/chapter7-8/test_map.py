# -*- coding:utf-8 -*-
"""
@project = 0522-1
@file = test_map
@author = Liangjisheng
@create_time = 2018/5/22 0022 下午 16:17
"""
def f1(x, y):
    return x, y

l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
l3 = map(f1, l1, l2)
print(list(l3))

def f2(x):
    return x * 2

print(list(map(f2, l1)))
print(list(map(f2, l2)))

def f3(x, y):
    return x * 2, y * 2

print(list(map(f3, l1, l2)))

# 在Python 3里,reduce()函数已经被从全局名字空间里移除了,它现在被放置在fucntools模块里
from functools import reduce
def f4(x, y):
    return x + y

# reduce函数，reduce函数会对参数序列中元素进行累积
print(reduce(f4, l1))       # 21

# function参数是一个有两个参数的函数，reduce依次从sequence中取一个元素，
# 和上一次调用function的结果做参数再次调用function。 第一次调用function时，
# 如果提供initial参数，会以sequence中的第一个元素和initial作为参数调用function，
# 否则会以序列sequence中的前两个元素做参数调用function
print(reduce(lambda x, y: x + y, [2, 3, 4, 5, 6], 1))   # 21
print(reduce(lambda x, y: x + y, [2, 3, 4, 5, 6]))      # 20
