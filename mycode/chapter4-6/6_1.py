# -*- coding:utf-8 -*-
"""
@project = 0523-1
@file = 6_1
@author = Liangjisheng
@create_time = 2018/5/23 0023 上午 9:04
"""
import random

def random_kid():
    return random.choice(['boy', 'girl'])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == 'girl':
        older_girl += 1
    if older == 'girl' and younger == 'girl':
        both_girls += 1
    if older == 'girl' or younger == 'girl':
        either_girl += 1

# 已知第一个孩子是女孩的情况下，两个孩子都是女孩的概率
print('P(both | older): ', both_girls / older_girl)     # 0.5007 ~ 1/2
# 已知至少有一个女孩的情况下，两个孩子都是女孩的概率
print('P(both | either): ', both_girls / either_girl)   # 0.3311 ~ 1/3
