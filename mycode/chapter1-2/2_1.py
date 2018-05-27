# -*- coding:utf-8 -*-
"""
@project = 0520-2
@file = 2_1
@author = Liangjisheng
@create_time = 2018/5/20 0020 下午 17:02
"""
import random
four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)
print(random.randrange(10))     # 从range(10) = [0, 1, ..., 9]中随机选取
print(random.randrange(3, 6))   # 从range(3, 6) = [3, 4, 5]中随机选取
up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten)

# 如果你需要不替换地（即不重复地）随机选择一个元素的样本，可以使用 random.sample
lottery_numbers = list(range(60))
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)
