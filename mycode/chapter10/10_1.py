# -*- coding:utf-8 -*-
"""
@project = 0526-2
@file = 10_1
@author = Liangjisheng
@create_time = 2018/5/26 0026 下午 16:52
"""
# 绘出直方图,即将你的数据分组成离散的区间(bucket),并对落入每个区间的数据点进行计数
import matplotlib.pyplot as plt
import math
from collections import Counter
import random
import numpy as np

def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size
    得到每个点对应的区间"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0  # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1  # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # consider the midpoint
        mid_p = normal_cdf(mid_z)  # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z

# 虑以下两个数据集

# -100到100之间均匀抽取
uniform = [200 * random.random() - 100 for _ in range(10000)]

# 均值为0标准差为57的正态分布
normal = [57 * inverse_normal_cdf(random.random())
          for _ in range(10000)]

np_uniform = np.array(list(uniform))
np_normal = np.array(normal)

print(np_uniform.mean())
print(np_uniform.std())
print(np_normal.mean())
print(np_normal.std())

plot_histogram(uniform, 10, '均匀分布的直方图')
plt.clf()
plot_histogram(normal, 10, '正态分布的直方图')
