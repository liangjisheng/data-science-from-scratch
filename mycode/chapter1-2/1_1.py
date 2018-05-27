# -*- coding:utf-8 -*-
"""
@project = 0519-1
@file = 1_1
@author = Liangjisheng
@create_time = 2018/5/19 0019 下午 19:07
"""
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]
# 用户的友邻关系
# 元组(0, 1)表示 id 为 0 的数据科学家 Hero 和 id 为 1 的数据科学家 Dunn 是朋友
friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
              (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# 对每个用户创建一个空的列表
for user in users:
    user['friend'] = []
# 用friendship数据填充
for i, j in friendship:
    users[i]['friend'].append(users[j])     # 把i加为j的朋友
    users[j]['friend'].append(users[i])     # 把j加为i的朋友

# 比如提问“平均的联系数是多少”（即每位用户平均拥有几位朋友）
# 首先计算出全部的联系数，这需要对所有用户的 friends 列表的长度求和
def number_of_friends(user):
    """how many friends does _user_have?"""
    return len(user['friend'])

total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)
# 然后，将它除以用户个数
num_users = len(users)
avg_connections = total_connections / num_users
print(avg_connections)

def getkey(userid_num_friend_tuple):
    return userid_num_friend_tuple[1]

# 创建一个列表(user_id, number_of_friends)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
print(num_friends_by_id)
result = sorted(num_friends_by_id,      # 排序数据
       # key=lambda user_id, num_friends: num_friends,
       key=getkey,      # 排序所用键
       reverse=True)    # 降序
# print(num_friends_by_id)
print(result)

# 对某个用户，依次计算每个朋友的朋友，最后合并结果
def friend_of_friend_ids_bad(user):
    # foaf是“朋友的朋友”的英文简写
    return [foaf['id'] for friend in user['friend'] for foaf in friend['friend']]

print(friend_of_friend_ids_bad(users[0]))

from collections import Counter

def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user['id'] != other_user['id']

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user['friend']
    that is, if he's not_the_same as all the people in user['friend']"""
    return all(not_the_same(friend, other_user) for friend in user['friend'])

def friends_of_friend_ids(user):
    return Counter(foaf['id']
                   for friend in user['friend']     # 对我的每一位朋友
                   for foaf in friend['friend']     # 计数他们的朋友
                   if not_the_same(user, foaf)      # 既不是我
                   and not_friends(user, foaf))     # 也不是我的朋友

print(friend_of_friend_ids_bad(users[3]))

# Counter({0: 2, 5: 1}) 这个输出结果正确无误地说明了 Chi（id 为 3）和
# Hero（id 为 0）有两个共同的朋友，和Clive（id 为 5）有一个共同的朋友
print(friends_of_friend_ids(users[3]))
