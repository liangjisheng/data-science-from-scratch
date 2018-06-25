# -*- coding:utf-8 -*-
"""
@project = 0624-1
@file = 19-1
@author = Liangjisheng
@create_time = 2018/6/24 0024 下午 16:24
"""
from functools import reduce
import math
import random

def vector_add(v, w):
    """adds two vectors componentwise"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
   return math.sqrt(squared_distance(v, w))


class KMeans:
    """performs k-means clustering"""
    def __init__(self, k):
        self.k = k              # 聚类的数目
        self.means = None       # 聚类的均值

    def classify(self, input):
        """return the index of the cluster closest to the input"""
        return min(range(self.k), key=lambda i: squared_distance(input, self.means[i]))

    def train(self, inputs):
        # 选择k个随机点作为初始的均值
        self.means = random.sample(inputs, self.k)
        assignments = None
        while True:
            # 查找新分配
            new_assignments = map(self.classify, inputs)

            # 如果所有数据点都不在被重新分配，那么就停止
            if assignments == new_assignments:
                return
            # 否则就重新分配
            assignments = new_assignments

            # 并基于新的分配计算新的均值
            for i in range(self.k):
                # 查找分配给聚类i的所有的点
                i_points = [p for p, a in zip(inputs, assignments) if a == i]
                # 确保i_points不是空的，因此除数不会是0
                if i_points:
                    self.means[i] = vector_mean(i_points)
