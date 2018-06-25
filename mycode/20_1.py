# -*- coding:utf-8 -*-
"""
@project = 0625-1
@file = 20_1
@author = Liangjisheng
@create_time = 2018/6/25 0025 下午 20:01
"""
import matplotlib.pyplot as plt

# 第一个数字代表它在招聘广告中出现的频次，第二个数字是在简历中出现的频次
data = [('big data', 100, 15), ('Hadoop', 95, 25), ('Python', 75, 50),
        ('R', 50, 40), ('machine learning', 80, 20), ('statistics', 20, 60),
        ("data science", 60, 70), ("analytics", 90, 3),
        ("team player", 85, 85), ("dynamic", 2, 90), ("synergies", 70, 0),
        ("actionable insights", 40, 30), ("think out of the box", 45, 10),
        ("self-starter", 30, 50), ("customer focus", 65, 15),
        ("thought leadership", 35, 35)]

# 利用水平位置表示其在招聘广告中的流行度， 用垂直位置表示其在简历中的流行度，
# 这样就能形象地传达一些信息
def text_size(total):
    """equal 8 if total is 0, 28 if total is 200"""
    return 8 + total / 200 * 20

for word, job_popularity, resume_popularity in data:
    plt.text(job_popularity, resume_popularity, word,
             ha='center', va='center',
             size=text_size(job_popularity + resume_popularity))
plt.xlabel("Popularity on Job Postings")
plt.ylabel("Popularity on Resumes")
plt.axis([0, 100, 0, 100])
plt.xticks([])
plt.yticks([])
plt.show()
