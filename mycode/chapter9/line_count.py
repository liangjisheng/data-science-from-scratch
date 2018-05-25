# -*- coding:utf-8 -*-
"""
@project = 0525-1
@file = line_count
@author = Liangjisheng
@create_time = 2018/5/25 0025 上午 11:25
"""
# 对收到的行数计数并输出计数结果
import sys

count = 0
for line in sys.stdin:
    count += 1

sys.stdout.write(str(count))

# 可以用这种方法来计数文件中有多少行包含数字。在 Windows 中，你可以用：
# type SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
# 而在 Unix 系统中，你可以用：
# cat SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
