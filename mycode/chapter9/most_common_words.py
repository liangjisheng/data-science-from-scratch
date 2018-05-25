# -*- coding:utf-8 -*-
"""
@project = 0525-1
@file = most_common_words
@author = Liangjisheng
@create_time = 2018/5/25 0025 上午 11:31
"""
# 这个脚本计算一个文件中，单词的数量并给出了最常用的单词
# 统计10个最常用的单词
# call in windows: type file_to_count | python most_common_words.py 10
#
#
import sys
from collections import Counter

# 传递单词的个数作为第一个参数
try:
    num_words = int(sys.argv[1])
except:
    print('usage: %s num_words' % sys.argv[0])
    sys.exit(1)     # 非0的exit代码表明有错误

counter = Counter(word.lower()               # 小写
                  for line in sys.stdin
                  for word in line.strip().split()      # 用空格划分
                  if word)                  # 跳过空的'words'

# 输出最常用的num_words个单词及个数
for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write('\t')
    sys.stdout.write(word)
    sys.stdout.write('\n')
