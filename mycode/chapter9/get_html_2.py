# -*- coding:utf-8 -*-
"""
@project = 0525-1
@file = get_html_2
@author = Liangjisheng
@create_time = 2018/5/25 0025 下午 15:24
"""
from bs4 import BeautifulSoup
import requests
html = requests.get('http://www.baidu.com').text
print(type(html))
soup = BeautifulSoup(html, 'html5lib')
print(type(soup))

with open('baidu.html', 'w') as f:
    # f.write(html)
    # f.write('\n')
    f.write(str(soup))



