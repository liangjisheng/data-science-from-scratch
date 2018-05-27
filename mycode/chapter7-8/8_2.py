# -*- coding:utf-8 -*-
"""
@project = 0524-2
@file = 8_2
@author = Liangjisheng
@create_time = 2018/5/24 0024 下午 19:36
"""
import random
import math

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
   return math.sqrt(squared_distance(v, w))


# 当 f 是一个多变量函数时，它有多个偏导数，每个偏导数表示仅有一个输入变量发生微小
# 变化时函数 f 的变化。
# 我们把导数看成是其第 i 个变量的函数，其他变量保持不变，以此来计算它第 i 个偏导数

def partial_difference_quotient(f, v, i, h):
    """compute the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0)     # 只对v的第i个元素增加h
         for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h

# 再以同样的方法估算它的梯度函数
def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]


# 很容易看出，当输入 v 是零向量时，函数 sum_of_squares 取值最小。但如果不知道输入是
# 什么，可以用梯度方法从所有的三维向量中找到最小值。我们先找出随机初始点，并在梯
# 度的反方向以小步逐步前进，直到梯度变得非常非常小
def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

# 这个函数为f(v) = sum(v_i ** 2 for v_i in v)
def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)

# 上面函数在各个方向的导数
def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

# 选取一个随机初始值
v = [random.randint(-10, 10) for i in range(3)]
print(v)
tolerance = 0.0000001

while True:
    gradient = sum_of_squares_gradient(v)   # 计算向量v的梯度
    next_v = step(v, gradient, -0.01)       # 取负的梯度步长
    if distance(next_v, v) < tolerance:     # 如果收敛了就停止
        break
    v = next_v                              # 否则继续迭代

# 如果运行以上程序,你会发现,它总是止于一个非常接近[0,0,0]的v值. tolerance值设
# 定得越小,v值就越接近[0,0,0]
print(v)


# 我们可以尝试一系列步长，并选出使目标函数值最小的那个步长来求其近似值
# 某些步长可能会导致函数的输入无效。所以，我们需要创建一个对无效输入值返回无限值
# (即这个值永远不会成为任何函数的最小值)的"安全应用"函数
def safe(f):
    """returns a new function that's the same as f,
    except that it outputs infinity whenever f produces an error"""
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')     # 意思是python中的无限值
        return safe_f
