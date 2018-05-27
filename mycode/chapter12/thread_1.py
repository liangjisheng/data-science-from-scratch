# -*- coding:utf-8 -*-
"""
@project = 0527-1
@file = thread_1
@author = Liangjisheng
@create_time = 2018/5/27 0027 上午 11:57
"""
import threading
import datetime

class ThreadClass(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print('%s says hello world at time: %s' % (self.getName(), now))

if __name__ == '__main__':
    for i in range(2):
        t = ThreadClass()
        t.start()
