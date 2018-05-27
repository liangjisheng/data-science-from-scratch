# -*- coding:utf-8 -*-
"""
@project = 0520-2
@file = 2_4
@author = Liangjisheng
@create_time = 2018/5/20 0020 下午 18:31
"""
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)
print(g(3))     # 8 (== ( 3 + 1) * 2)
print(g(-1))

def f2(x, y):
    return x + y

def magic(*args, **kwargs):
    print('unnamed args:', args)
    print('keyword args:', kwargs)

magic(1, 2, key='word', key2='word2')

# args是一个它的未命名参数的元组,而kwargs是一个它的已命名参数的dict.
# 反过来也适用,你可以使用一个list(或者tuple)和dict来给函数提供参数
def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {'z': 3}
print(other_way_magic(*x_y_list, **z_dict))

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print(g(1, 2))
