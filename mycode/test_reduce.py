# -*- coding:utf-8 -*-
"""
@project = 0522-1
@file = test_reduce
@author = Liangjisheng
@create_time = 2018/5/22 0022 下午 16:12
"""
def f1(x):
    if x > 20:
        return True
    else:
        return False

l1 = [1, 2, 3, 42, 67, 16]
# print(filter(f1, l1))
# print(list(filter(f1, l1)))
l2 = filter(f1, l1)
print(l2)
print(l2.__next__())
print(l2.__next__())
# print(l2.__next__())      # StopIteration

