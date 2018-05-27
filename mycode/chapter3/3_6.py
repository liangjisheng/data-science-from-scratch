# -*- coding:utf-8 -*-
"""
@project = 0521-1
@file = 3_6
@author = Liangjisheng
@create_time = 2018/5/21 0021 下午 19:43
"""
# 当你分散了可比较的变量，如果让 matplotlib 选择刻度，可能会得到一个误导性的图
from matplotlib import pyplot as plt

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

# 如果引入对plt.axis("equal")的调用,会更精确地显示大多数变化是发生在测验2上的
plt.axis('equal')

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("测验1的分数")
plt.ylabel("测验2的分数")
plt.show()
