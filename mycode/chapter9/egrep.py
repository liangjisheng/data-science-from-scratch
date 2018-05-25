# -*- coding:utf-8 -*-
"""
@project = 0525-1
@file = egrep
@author = Liangjisheng
@create_time = 2018/5/25 0025 上午 11:23
"""
import re
import sys

# sys.argv是命令行参数的列表
# sys.argv[0]是程序自己的名字
# sys.argv[1]是在命令行上指定的正则表达式
regex = sys.argv[1]

# 对传递到这个脚本中的每一行
for line in sys.stdin:
    # 如果找到，则把它写入stdout
    if re.search(regex, line):
        sys.stdout.write(line)

# 可以用这种方法来计数文件中有多少行包含数字。在 Windows 中，你可以用：
# type SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
# 而在 Unix 系统中，你可以用：
# cat SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
