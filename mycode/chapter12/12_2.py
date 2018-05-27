# -*- coding:utf-8 -*-
"""
@project = 0527-1
@file = 12_2
@author = Liangjisheng
@create_time = 2018/5/27 0027 下午 16:56
"""
# 在更高的维度上， k近邻法会因为“维数灾难”而遇到麻烦，其根源在于高维空间过于巨
# 大。高维空间内的点根本不会表现得彼此邻近。 观察维数灾难的一种方法是在一个高维度
# 的 d 维空间“单位立方体”上随机地生成数据点对，并计算它们之间的距离
import random
import matplotlib.pyplot as plt
from share import *

# 生成dim维空间上单位立方体的随机数据点
def random_point(dim):
    return [random.random() for _ in range(dim)]

def random_distance(dim, num_pairs):
    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]

# 对从1到100的每一个维度，我们会计算10000个距离，并使用它们计算每个维度上
# 点和点之间的平均距离和最小距离
dimensions = range(1, 101)
avg_distances = []
min_distances = []
random.seed(0)      # 固定种子，使得每次生成的随机数都一样

for dim in dimensions:
    distances = random_distance(dim, 10000)     # 10000个随机对
    avg_distances.append(mean(distances))        # 追踪平均值
    min_distances.append(min(distances))         # 追踪最小值

plt.plot(dimensions, avg_distances, color='b', label='平均距离')
plt.plot(dimensions, min_distances, color='g', label='最小距离')
plt.xlabel('维度的个数')
plt.title('10000个随机距离')
# 从图中可看出,随着维数的增加,点和点之间的平均距离也增加了,这是维数的一个灾难
plt.show()

# 但更麻烦的是最近距离和平均距离之间的比例
plt.clf()
min_avg_ratio = [min_dist / avg_dist
                 for min_dist, avg_dist in zip(min_distances, avg_distances)]
plt.plot(dimensions, min_avg_ratio)
plt.xlabel('维度的个数')
plt.title('最小距离/平均距离')
# 随着维数的增加，最小距离/平均距离的比值越来越接近1
plt.show()
