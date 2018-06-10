# -*- coding:utf-8 -*-
"""
@project = 0529-1
@file = 13_1
@author = Liangjisheng
@create_time = 2018/5/29 0029 上午 10:27
"""
import re
from collections import defaultdict
import math

# 到目前为止，我们已经学习了构建垃圾邮件分类器所需的各方面的知识。下面，我们首先
# 建立一个简单的函数， 来将邮件解析为不同的单词。首先要把各个邮件文本转换为小写形
# 式,然后使用re.findall()提取由字母、数字和撇号组成的“单词”，最后使用set()函
# 数获得不同的单词
def tokenize(message):
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)

# 我们的第二个函数用来计算单词出现在已做标记的邮件训练集中的次数。该函数将返回一
# 个字典，其键为单词，其值为列表，该列表包含两个元素 [spam_count, non_spam_count]，
# 分别表示该单词出现在垃圾邮件和非垃圾邮件中的次数
def count_words(training_set):
    """training set consists of pairs (message, is_spam)"""
    counts = defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts

# 接下来，我们利用前面讲过的平滑技术将这些计数转换为估计概率。函数将返回一个列
# 表，列表元素包含三方面的内容， 分别是各个单词、该单词出现在垃圾邮件中的概率以及
# 该单词出现在非垃圾邮件中的概率
def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
    """turn the word_counts into a list of triplets
    w, p(w | spam) and p(w | ~spam)"""
    return [(w, (spam + k) / (total_spams + 2 * k),
            (non_spam + k) / (total_non_spams + 2 * k))
            for w, (spam, non_spam) in counts.iteritems()]

# 最后要做的事情是利用这些单词的概率（以及朴素贝叶斯假设）给邮件赋予概率
def spam_probability(word_probs, message):
    message_words = tokenize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0

    # 迭代词汇表中的每一个单词
    for word, prob_if_spam, prob_if_not_spam in word_probs:

        # 如果word出现在了邮件中，则增加看到它的对数概率
        if word in message_words:
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)

        # 如果word没有出现在邮件中,则增加看不到它的对数概率,也就是log(1 - 看到它的概率)
        else:
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)

    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)


class NaiveBayesClassifier(object):
    """朴素贝叶斯分类器"""
    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []

    def train(self, training_set):
        # 对垃圾邮件和非垃圾邮件计数
        num_spams = len([is_spam
                         for message, is_spam in training_set
                         if is_spam])
        num_non_spams = len(training_set) - num_spams

        # 通过pipeline运行训练数据
        word_counts = count_words(training_set)
        self.word_probs = word_probabilities(word_counts, num_spams,
                                             num_non_spams, self.k)

    def classify(self, message):
        return spam_probability(self.word_probs, message)
