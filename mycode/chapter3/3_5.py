# -*- coding:utf-8 -*-
"""
@project = 0521-1
@file = 3_5
@author = Liangjisheng
@create_time = 2018/5/21 0021 下午 19:30
"""
# 散点图是显示成对数据集的可视化关系的好选择。下图显示了你的用户们已有的
# 朋友数和他们每天花在网站上的分钟数之间的关系
from matplotlib import pyplot as plt

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# 每个点加标记
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),   # 把标记放在对应的点上
                 xytext=(5, -5),        # 但要有轻微偏离
                 textcoords='offset points')

plt.title("日分钟数与朋友数")
plt.xlabel("朋友数")
plt.ylabel("花在网站上的日分钟数")
plt.show()
