# -*- coding:utf-8 -*-
"""
@project = 0526-1
@file = 9_1
@author = Liangjisheng
@create_time = 2018/5/26 0026 下午 15:37
"""
from bs4 import BeautifulSoup
import requests

url = 'https://www.safaribooksonline.com/topics/analytics?sortby=Date+Added&page=1'
# url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page=1"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')
print(type(soup))
print(len(soup))
# print(soup)

# 会看到每本书（或每部视频）都唯一地包含在一个表格单元格元素<td>中,它的类是thumbtext
# 良好的开端是找到所有的 td thumbtext 标签元素
tds = soup('td', 'thumbtext')
print(len(tds))
