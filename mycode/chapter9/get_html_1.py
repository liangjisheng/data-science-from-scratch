# -*- coding:utf-8 -*-
"""
@project = 0525-1
@file = get_html_1
@author = Liangjisheng
@create_time = 2018/5/25 0025 下午 14:52
"""
from bs4 import BeautifulSoup
import requests
html = requests.get('http://www.example.com').text
print(type(html))
soup = BeautifulSoup(html, 'html5lib')
print(type(soup))

# with open('h1.html', 'w') as f:
    # f.write(str(html))
    # f.write('\n')
    # f.write(str(soup))

# 完成上面的步骤后，可以用一些简单的方法得到完美的解析
# 通常我们会处理一些 Tag 对象，它们对应于 HTML 页面结构的标签表示
# 比如，找到你能用的第一个<p>标签(及其内容)
first_paragraph = soup.find('p')    # 或仅仅soup.p
# 获取文本
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()
print(len(first_paragraph_words))
print(first_paragraph_words)

# 另外可以把标签当作字典来提取其属性
# first_paragraph_id = soup.p['id']     # 如果没有'id'则报KeyError
first_paragraph_id = soup.p.get('id')       # 如果没有'id'则返回None
print(type(first_paragraph_id))
print(first_paragraph_id)

# 可以一次得到多个标签
all_paragraphs = soup.find_all('p')     # 或仅仅soup('p')
print(type(all_paragraphs))

paragraphs = [p for p in soup('p')]
print(type(paragraphs))
print(len(paragraphs))
print(paragraphs)

paragraphs_with_ids = [p for p in all_paragraphs if p.get('id')]
print(type(paragraphs_with_ids))
print(len(paragraphs_with_ids))
print(paragraphs_with_ids)
