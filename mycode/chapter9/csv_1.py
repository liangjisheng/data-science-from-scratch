# -*- coding:utf-8 -*-
"""
@project = 0525-1
@file = csv_1
@author = Liangjisheng
@create_time = 2018/5/25 0025 下午 14:16
"""
import csv

def process(date, symbol, closing_price):
    print(date, symbol, closing_price)

with open('tab_delimited_stock_prices.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        # print(row)
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)

print()

# 文件存在头部,你既可以跳过头部的行(利用对read.next()的初始调用)也可以利用
# csv.DictReader把每一行读成字典(把头部作为关键字)
with open('colon_delimited_stock_prices.txt', 'r') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        print(row)
        date = row['date']
        symbol = row['symbol']
        closing_price = float(row['closing_price'])
        process(date, symbol, closing_price)

print()

# 用csv.writer写文件
today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}
with open('comma_delimited_stock_prices.txt', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])
