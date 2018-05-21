# -*- coding:utf-8 -*-
"""
@project = 0521-1
@file = 3_1
@author = Liangjisheng
@create_time = 2018/5/21 0021 下午 16:54
"""
from matplotlib import pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# 创建一幅线图，x轴是年份，y轴是gdp
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# 添加一个标题
plt.title('名义GDP')
# y轴加标记
plt.ylabel('十亿美元')
plt.show()
plt.clf()   # 清除画布

# 输出字体列表
# import matplotlib
# print(sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist]))

# 几部电影所获得的奥斯卡金像奖的数目
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# 条形的默认宽度是0.8，因此我们对左侧坐标加上0.1
# 这样每个条形就被放置在中心了
xs = [i + 0.1 for i, _ in enumerate(movies)]

# 使用左侧x坐标[xs]和高度[num_oscars]画条形图
plt.bar(xs, num_oscars)
plt.title('所获奥斯卡金像奖数量')

# 使用电影的名字标记x轴，位置在x轴上条形的中心
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
plt.show()
