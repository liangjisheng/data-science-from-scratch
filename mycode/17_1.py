# -*- coding:utf-8 -*-
"""
@project = 0606-1
@file = 17_1
@author = Liangjisheng
@create_time = 2018/6/6 0006 下午 19:07
"""
import math
from collections import Counter, defaultdict
from functools import partial

# 根据一组概率计算熵 H(S)=-p1log2p1-…-pnlog2p
def entropy(class_probabilities):
    """given a list of class probabilities, compute the entropy"""
    return sum(-p * math.log(p, 2)
               for p in class_probabilities
               if p)        # 忽略0可能性

# 计算类别的概率
def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count
            for count in Counter(labels).values()]

# 计算一组数据的熵
def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

# 我们希望通过某种方法对数据集的分割效果来表示熵。对于某个划分方法，如果
# 得到的子集的熵较低（即确定性很高）的话，我们就说这个划分方法的熵较低；反之，如
# 果得到的子集的（数量很多并且）熵较高（即不确定性很高）的话，我们就说这个划分方
# 法的熵较高

# 计算一个划分的熵 H=q1H(S1)+…+qmH(Sm)
def partition_entropy(subsets):
    """find the entropy from the partition of data into subsets
    subsets is a list of lists of labeled data"""

    total_count = sum(len(subset) for subset in subsets)
    return sum(data_entropy(subset) * len(subset) / total_count
               for subset in subsets)

inputs = [
    ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, False),
    ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'yes'}, False),
    ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, False),
    ({'level': 'Mid', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, True),
    ({'level': 'Senior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, False),
    ({'level': 'Senior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Senior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'yes'}, True),
    ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, True),
    ({'level': 'Mid', 'lang': 'Java', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, False)
]

# 根据某个属性的值分割输入数据集
def partition_by(inputs, attribute):
    """each input is a pair (attribute_dict, label).
    return a dict: attribute_value -> inputs"""
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][attribute]       # 得到特定属性的值
        groups[key].append(input)       # 然后把这个输入加到正确的列表中
    return groups

# 计算根据某个属性的值分割数据集后的划分熵
def partition_entropy_by(inputs, attribute):
    """computes the entropy corresponding to the given partition"""
    partitions = partition_by(inputs, attribute)
    print(partitions)
    return partition_entropy(partitions.values())

# 找出在整个数据集上具有最小熵的分割
for key in ['level', 'lang', 'tweets', 'phd']:
    print(key, partition_entropy_by(inputs, key))
print()
# level 0.693536138896
# lang 0.860131712855
# tweets 0.788450457308
# phd 0.892158928262

# 利用 level 进行的分割的熵最小，所以我们需要为每一个可能的 level 值建立
# 一个子树。所有 Mid 应聘者都被标记成了 True，这意味着 Mid 子树是一个叶节点，其预测
# 结果为 True。对于 Senior 级别的求职者，其标签既有 True 也有 False，所以我们需要进一
# 步划分:
senior_inputs = [(input, label)
                 for input, label in inputs if input['level'] == 'Senior']
for key in ['lang', 'tweets', 'phd']:
    print(key, partition_entropy_by(senior_inputs, key))
print()
# lang 0.4
# tweets 0.0
# phd 0.9509775004326938
# 这表明，我们下一步应该根据 tweets 进行分割，因为它能得到熵为 0 的分割。对于 Senior
# 级别的应聘者， tweets 的值为“yes”的最终分类结果为 True，而 tweets 的值为“no”的
# 最终分类结果为 False


# 最后，如果我们对 Junior 级别的应聘者做同样的事情，最终会根据属性 phd 进行划分，并
# 且发现没有博士学位的结果都是 True，拥有博士学位的结果都是 False
Junior_inputs = [(input, label)
                 for input, label in inputs if input['level'] == 'Junior']
for key in ['lang', 'tweets', 'phd']:
    print(key, partition_entropy_by(Junior_inputs, key))
print()
# lang 0.9509775004326938
# tweets 0.9509775004326938
# phd 0.0


# 将树定义为下列情况之一
# True
# False
# 元组 (attribute, subtree_dict)
# 这里的 True 代表一个叶节点，对于任何输入该节点都会返回 True； False 也表示一个叶节
# 点，但是对于任何输入该节点都会返回 False；而元组则代表一个决策节点，对于任何输
# 入，该节点都会根据 attribute 的值利用相应的子树对输入进行分类。
# 使用这种方法，我们的招聘决策树将表示如下
# ('level',
#   {'Junior': ('phd', {'no': True, 'yes': False}),
#   'Mid': True,
#   'Senior': ('tweets', {'no': False, 'yes': True})})


# 给定了表示方法后，我们就可以对输入进行分类了
def classify(tree,  input):
    """classify the input using the given decision tree"""

    # 如果这是一个叶节点，则返回其值
    if tree in [True, False]:
        return tree

    # 否则这个树就包含一个需要划分的属性和一个字典，
    # 字典的键是那个属性的值，字典的值是下一步需要考虑的子树
    attribute, subtree_dict = tree
    # 如果输入的是缺失的属性，则返回None
    subtree_key = input.get(attribute)

    if subtree_key not in subtree_dict:     # 如果键没有子树
        subtree_key = None                  # 则需要用到None子树

    subtree = subtree_dict[subtree_key]     # 选择恰当的子树
    return classify(subtree, input)         # 并用它来对输入分类


# 最后要做的就是利用训练数据建立决策树的具体表示形式

# 如果所有数据都有相同的标签， 那么创建一个预测最终结果即为该标签所示的叶节点,然后停止
# 如果属性列表是空的（即已经没有更多的问题可提问了），就创建一个预测结果为最常见的标签的叶节点，然后停止
# 否则，尝试用每个属性对数据进行划分
# 选择具有最低划分熵的那次划分的结果
# 根据选定的属性添加一个决策节点
# 针对划分得到的每个子集，利用剩余属性重复上述过程
def build_tree_id3(inputs, split_candidates=None):
    # 如果这是第一步，第一次输入的所有的键就都是split_candidates
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()

    # 对输入里的True和False计数
    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label])
    num_false = num_inputs - num_trues

    if 0 == num_trues:      # 若没有True，则返回一个"False"叶节点
        return False
    if 0 == num_false:      # 若没有False，则返回一个"True"叶节点
        return True

    if not split_candidates:        # 若不再有split_candidates
        return num_trues >= num_false   # 则返回多数叶节点

    # 否则在最好的属性上进行划分
    best_attribute = min(split_candidates,
                         key=partial(partition_entropy_by, inputs))

    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates if a != best_attribute]

    # 递归的创建子树
    subtrees = {attribute_value: build_tree_id3(subset, new_candidates)
                for attribute_value, subset in partitions.items()}

    subtrees[None] = num_trues > num_false      # 默认情况
    return best_attribute, subtrees


# 在我们所建的树上，每一个叶节点要么由清一色的 True 输入组成，要不就是由清一色的
# False 输入组成。这意味着，该决策树对于这个训练数据集的预测效果堪称完美
tree = build_tree_id3(inputs)
print(tree)

test1 = {"level": "Junior", "lang": "Java", "tweets": "yes", "phd": "no"}
print(classify(tree, test1))        # True
test2 = {"level": "Junior", "lang": "Java", "tweets": "yes", "phd": "yes"}
print(classify(tree, test2))        # False
print()

# 同时，也可以将它应用于具有缺失值或非预期值的数据
print(classify(tree, {"level": "Intern"}))     # True
print(classify(tree, {"level": "Senior"}))     # False

# 由于我们的目的主要是演示如何构建决策树，因此这里使用了整个数据集来
# 建立决策树。 与往常一样，如果现实中我们想创造一个优秀模型的话，就应
# 该（收集更多的数据并且）将数据分成训练子集、验证子集和测试子集
