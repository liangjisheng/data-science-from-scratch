# -*- coding:utf-8 -*-
"""
@project = 0520-2
@file = 2_3
@author = Liangjisheng
@create_time = 2018/5/20 0020 下午 17:30
"""
def exp(base, power):
    return base ** power

print(exp(2, 3))

def two_to_the(power):
    return exp(2, power)

print(two_to_the(3))

# 一个另辟蹊径的方法是使用 functools.partial
from functools import partial
two_to_the_1 = partial(exp, 2)
print(two_to_the_1(3))

# 如果你为后面的参数指定了名字，也能用 partial 来填充这些参数
square_of = partial(exp, power=2)
print(square_of(3))
print()

def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
print(twice_xs)
twice_xs1 = list(map(double, xs))
print(twice_xs1)
list_doubler = partial(map, double)
twice_xs2 = list(list_doubler(xs))
print(twice_xs2)
print()

# 如果你提供了多个列表，可以对带有多个参数的函数使用 map
def multiply(x, y):
    return x * y

products = list(map(multiply, [1, 2], [4, 5]))
print(products)

# 类似地， filter 做了列表解析中 if 的工作
def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]
print(x_evens)
x_evens1 = list(filter(is_even, xs))
print(x_evens1)
list_evener = partial(filter, is_even)
x_evens2 = list(list_evener(xs))
print(x_evens2)

from functools import reduce
x_product = reduce(multiply, xs)  # = 1 * 2 * 3 * 4 = 24
print(x_product)
list_product = partial(reduce, multiply)  # reduce了一个列表的*function*
x_product = list_product(xs)  # 同样是24
print(x_product)
