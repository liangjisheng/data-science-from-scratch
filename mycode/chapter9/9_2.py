# -*- coding:utf-8 -*-
"""
@project = 0526-1
@file = 9_2
@author = Liangjisheng
@create_time = 2018/5/26 0026 下午 15:54
"""
# 我们会用到它的loads函数，这个函数可以把一个代表JSON对象的字符串反串行化
# (deserialize)为Python对象
import json
serialized = """{ "title" : "Data Science Book",
                    "author" : "Joel Grus",
                    "publicationYear" : 2014,
                    "topics" : [ "data", "science", "data science"] }"""

# 解析JSON创建一个Python字典
deserialized = json.loads(serialized)
print(type(serialized))         # str
print(type(deserialized))       # dict
if "data science" in deserialized['topics']:
    print(deserialized)

dict1 = {"title": "Data Science Book",
                    "author": "Joel Grus",
                    "publicationYear": 2014,
                    "topics": ["data", "science", "data science"]}
print(dict1)
