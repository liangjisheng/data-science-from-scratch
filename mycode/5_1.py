# -*- coding:utf-8 -*-
"""
@project = 0522-1
@file = 5_1
@author = Liangjisheng
@create_time = 2018/5/22 0022 下午 16:59
"""
import re, math, random
from collections import Counter, defaultdict
from matplotlib import pyplot as plt
from functools import partial

num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

friend_counts = Counter(num_friends)
xs = list(range(101))
ys = [friend_counts[x] for x in xs]     # height刚好是朋友的个数

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("朋友数的直方图")
plt.xlabel("朋友个数")
plt.ylabel("人数")
plt.show()

# 数据点个数
num_point = len(num_friends)    # 204
print(num_point)

# 最大值最小值
largest_value = max(num_friends)
smallest_value = min(num_friends)
print(largest_value)
print(smallest_value)

# 如果你想知道特定位置的值，可以这样做
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]  # 1
second_smallest_value = sorted_values[1]  # 1
second_largest_value = sorted_values[-2]  # 49

# 均值
def mean(x):
    return sum(x) / len(x)

print(mean(num_friends))

# 中位数
def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # 如果是奇数，返回中间两个值的均值
        return sorted_v[midpoint]
    else:
        # 如果是偶数，返回中间两个值的均值
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print(median(num_friends))

# 分位数
def quantile(x, p):
    """return the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

print(quantile(num_friends, 0.10))
print(quantile(num_friends, 0.25))
print(quantile(num_friends, 0.75))
print(quantile(num_friends, 0.90))

# 众数(mode),它是指出现次数最多的一个或多个数
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

print(mode(num_friends))

# 极差(range)指最大元素与最小元素的差
def data_range(x):
    return max(x) - min(x)

print(data_range(num_friends))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

# 方差
def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

print(variance(num_friends))

# 标准差(standard deviation)
def standard_deviation(x):
    return math.sqrt(variance(x))

print(standard_deviation(num_friends))

# 极差和标准差也都有我们之前提到的均值计算常遇到的异常值问题
# 一种更加稳健的方案是计算 75% 的分位数和 25% 的分位数之差
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

print(interquartile_range(num_friends))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

print(len(daily_minutes))

# 协方差（covariance），这个概念是方差的一个对应词。方差衡量了单个变
# 量对均值的偏离程度，而协方差衡量了两个变量对均值的串联偏离程度
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

print(covariance(num_friends, daily_minutes))

# 相关是更常受到重视的概念，它是由协方差除以两个变量的标准差
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0    # 如果没有变动，相关系数为0

print(correlation(num_friends, daily_minutes))

plt.scatter(num_friends, daily_minutes)
plt.xlabel('朋友数')
plt.ylabel('分钟/天')
plt.title('有异常值的相关系数')
plt.show()

# 图中那个有100个朋友的用户(每天只在网上花费1分钟)是一个明显的异常值，
# 相关系数的计算对异常值非常敏感。如果我们计算时希望忽略这个人
outlier = num_friends.index(100)    # outlier的索引
num_friends_good = [x for i, x in enumerate(num_friends)
                    if i != outlier]
daily_minutes_good = [x for i, x in enumerate(daily_minutes)
                      if i != outlier]

print(correlation(num_friends_good, daily_minutes_good))

plt.clf()
plt.scatter(num_friends_good, daily_minutes_good)
plt.xlabel('朋友数')
plt.ylabel('分钟/天')
plt.title('移除异常值之后的相关系数')
plt.show()