# -*- coding:utf-8 -*-
"""
@project = 0521-1
@file = 3_3
@author = Liangjisheng
@create_time = 2018/5/21 0021 下午 19:11
"""
# 在使用plt.axis()时要谨慎.在创建条形图时,y轴不从 0 开始是一种特别不好的形式
# 因为这很容易误导人
from matplotlib import pyplot as plt
mentions = [500, 505]
years = [2013, 2014]
plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("听到有人提及‘数据科学’的次数")

# 如果不这么做，matplotlib会把x轴的刻度标记为0和1
# 然后会在角上加上+2.013e3(糟糕的matplotlib操作!)
plt.ticklabel_format(useOffset=False)

# 这会误导y轴只显示500以上的部分
plt.axis([2012.5, 2014.5, 499, 506])
# plt.axis([2012.5, 2014.5, 0, 600])
plt.title("快看如此'巨大'的增长！ ")
plt.show()
