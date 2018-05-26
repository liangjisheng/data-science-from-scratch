# -*- coding:utf-8 -*-
"""
@project = 0526-2
@file = 10_3
@author = Liangjisheng
@create_time = 2018/5/26 0026 下午 17:36
"""
def parse_row(input_row, parsers):
    """given a list of parsers (some of which may be None)
    apply the appropriate one to each element of the input_row"""

    return [parser[value] if parser is not None else value
            for value, parser in zip(input_row, parsers)]

def parse_rows_with(reader, parsers):
    """wrap a reader to apply the parsers to each of its rows"""
    for row in reader:
        yield parse_row(row, parsers)

# 我们通常会使用一个None函数而非硬跑程序。我们可以通过一个辅助函数来解决
def try_or_none(f):
    """wraps f to return None if f raises an exception
    assumes f takes only one input"""
    def f_or_none(x):
        try:
            return f(x)
        except:
            return None
    return f_or_none

# 然后我们重写 parse_row 来使用它
def parse_row(input_row, parsers):
    return [try_or_none(parser)(value) if parser is not None else value
            for value, parser in zip(input_row, parsers)]

import dateutil.parser
import csv
data = []

with open('comma_delimited_stock_prices.csv', 'r') as f:
    reader = csv.reader(f)
    for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
        data.append(line)

# 然后我们只需检查其中 None 的行数
for row in data:
    if any(x is None for x in row):
        print(row)
