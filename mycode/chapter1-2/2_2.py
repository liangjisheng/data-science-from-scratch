# -*- coding:utf-8 -*-
"""
@project = 0520-2
@file = 2_2
@author = Liangjisheng
@create_time = 2018/5/20 0020 下午 17:24
"""
class Set(object):
    # 这些是成员函数
    # 每个函数都取第一个参数"self" （另一种惯例）
    # 它表示所用到的特别的集合对象

    def __init__(self, values=None):
        """This is the constructor.
        It gets called when you create a new Set.
        You would use it like
        s1 = Set() # 空集合
        s2 = Set([1,2,2,3]) # 用值初始化"""
        self.dict = {} # Set的每一个实例都有自己的dict属性
        # 我们会用这个属性来追踪成员关系
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """this is the string representation of a Set object
        if you type it at the Python prompt or pass it to str()"""
        return "Set: " + str(self.dict.keys())

    # 通过成为self.dict中对应值为True的键，来表示成员关系
    def add(self, value):
        self.dict[value] = True

    # 如果它在字典中是一个键，那么在集合中就是一个值
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

s = Set([1, 2, 3])
print(s)
s.add(4)
print(s)
print(s.contains(4))
s.remove(3)
print(s.contains(3))
print(s)
