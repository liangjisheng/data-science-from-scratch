# -*- coding:utf-8 -*-
"""
@project = 0526-1
@file = 9_3
@author = Liangjisheng
@create_time = 2018/5/26 0026 下午 16:02
"""
import json
import requests
# 日期解析
from dateutil.parser import parse
from collections import Counter

# endpoint = 'https://api.github.com/users/joelgrus/repos'
endpoint = 'https://api.github.com/users/liangjisheng/repos'
# repos 是一个 Python 字典的列表，其中每一个字典表示我的 GitHub 账户的一个代码仓库
repos = json.loads(requests.get(endpoint).text)
print(type(repos))          # list
print(len(repos))           # 7
print(type(repos[0]))       # dict
print(len(repos[0]))        # 71    每个代码仓库由71个属性描述

dates = [parse(repo['created_at']) for repo in repos]
# print(dates)
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)
print(month_counts)
print(weekday_counts)

# 获取我最后五个代码仓库所用的语言
last_5_repositories = sorted(repos, key=lambda r: r['created_at'], reverse=True)[:5]
last_5_languages = [repo['language'] for repo in last_5_repositories]
print(last_5_languages)
