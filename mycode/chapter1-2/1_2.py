# -*- coding:utf-8 -*-
"""
@project = 0519-1
@file = 1_2
@author = Liangjisheng
@create_time = 2018/5/19 0019 下午 20:05
"""
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# 某种事物有共同爱好的用户
def datas_scientists_who_like(target_interest):
    return [user_id for user_id, user_interest in interests
            if user_interest == target_interest]


from collections import defaultdict
from collections import Counter

# 建立从兴趣到用户的索引
# 键是interest，值是带有这个interest的user_id的列表
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
print(user_ids_by_interest)

# 建立从用户到兴趣的索引
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
print(interests_by_user_id)

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user['id']]
                   for interested_user_id in user_ids_by_interest[interest]
                   if user['id'] != interested_user_id)

# Counter({9: 3, 1: 2, 8: 1, 5: 1})
# 用户0与用户9有3个共同的兴趣
print(most_common_interests_with({"id": 0, "name": "Hero"}))

# 数一下兴趣词汇的个数
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())
print(words_and_counts)
# 列出出现一次以上的词汇
for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
