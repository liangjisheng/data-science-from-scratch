# -*- coding:utf-8 -*-
"""
@project = 0610-1
@file = 18_1
@author = Liangjisheng
@create_time = 2018/6/10 0010 下午 12:18
"""
import math
import random
import matplotlib
import matplotlib.pyplot as plt

# sigmoid 函数
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# 计算两个向量点乘
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# 神经元输出
def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))

# 神经网络可以用（权重）列表的（神经元）列表的（层）列表来表示
# 前馈神经网络
def feed_forward(neural_network, input_vector):
    """takes in a neural network
    (represented as a list of lists of lists of weights)
    and returns the output from forward-propagating the input"""
    outputs = []

    # 每次处理一层
    for layer in neural_network:
        input_with_bias = input_vector + [1]        # 增加一个偏倚输入
        output = [neuron_output(neuron, input_with_bias)    # 计算输出
                  for neuron in layer]                      # 每一个神经元
        outputs.append(output)

        # 然后下一层的输入就是这一层的输出
        input_vector = output

    return outputs


def backpropagate(network, input_vector, targets):
    hidden_outputs, outputs = feed_forward(network, input_vector)

    # the output * (1 - output) is from the derivative of sigmoid
    output_deltas = [output * (1 - output) * (output - targets[i])
                     for i, output in enumerate(outputs)]

    # adjust weights for output layer (network[-1]), one neuron at a time
    for i, output_neuron in enumerate(network[-1]):
        # focus on the ith output layer neuron
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            # adjust the jth weight based on both
            # this neuron's delta and its jth input
            output_neuron[j] -= output_deltas[i] * hidden_output

    # back-propagate errors to hidden layer
    hidden_deltas = [hidden_output * (1 - hidden_output) *
                     dot(output_deltas, [n[i] for n in network[-1]])
                     for i, hidden_output in enumerate(hidden_outputs)]

    # adjust weights for hidden layer (network[0]), one neuron at a time
    for i, hidden_neuron in enumerate(network[0]):
        for j, input in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input


xor_network = [# hidden layer
                [[20, 20, -30],     # and神经元
                 [20, 20, -10]],    # or神经元
                # output layer
                [[-60, 60, -30]]]   # 第二次输入不同于第一次输入神经元

for x in [0, 1]:
    for y in [0, 1]:
        # feed_forward生成每个神经元的输出
        # feed_forward[-1]是每个输出层神经元的输出
        res = x, y, feed_forward(xor_network, [x, y])
        # print(res)
        # print(res[-1])
        # print()

def patch(x, y, hatch, color):
    """return a matplotlib 'patch' object with the specified
    location, crosshatch pattern, and color"""
    return matplotlib.patches.Rectangle((x - 0.5, y - 0.5), 1, 1,
                                        hatch=hatch, fill=False, color=color)

def show_weights(neuron_idx):
    weights = network[0][neuron_idx]
    abs_weights = list(map(abs, weights))
    grid = [abs_weights[row:(row + 5)]    # turn the weights into a 5x5 grid
            for row in range(0, 25, 5)]   # [weights[0:5], ..., weights[20:25]]

    ax = plt.gca()  # to use hatching, we'll need the axis

    ax.imshow(grid,     # here same as plt.imshow
              cmap=matplotlib.cm.binary,    # use white-black color scale
              interpolation='none')     # plot blocks as blocks

    # cross-hatch the negative weights
    for i in range(5):  # row
        for j in range(5):  # column
            if weights[5*i + j] < 0:    # row i, column j = weights[5*i + j]
                # add black and white hatches, so visible whether dark or light
                ax.add_patch(patch(j, i, '/', "white"))
                ax.add_patch(patch(j, i, '\\', "black"))
    plt.show()


if __name__ == '__main__':
    raw_digits = [
        """11111
           1...1
           1...1
           1...1
           11111""",

        """..1..
           ..1..
           ..1..
           ..1..
           ..1..""",

        """11111
           ....1
           11111
           1....
           11111""",

        """11111
           ....1
           11111
           ....1
           11111""",

        """1...1
           1...1
           11111
           ....1
           ....1""",

        """11111
           1....
           11111
           ....1
           11111""",

        """11111
           1....
           11111
           1...1
           11111""",

        """11111
           ....1
           ....1
           ....1
           ....1""",

        """11111
           1...1
           11111
           1...1
           11111""",

        """11111
           1...1
           11111
           ....1
           11111"""]

    def make_digit(raw_digit):
        return [1 if c == '1' else 0
                for row in raw_digit.split("\n")
                for c in row.strip()]

    inputs = list(map(make_digit, raw_digits))

    targets = [[1 if i == j else 0 for i in range(10)]
               for j in range(10)]

    random.seed(0)  # 得到重复的结果
    input_size = 25  # 每个输入都是长度为25的向量
    num_hidden = 5  # 隐藏层将含有5个神经元
    output_size = 10  # 对于每个输入，需要10个输出结果

    # 每个隐藏神经元对每个输入都有一个权重和偏倚权重
    hidden_layer = [[random.random() for __ in range(input_size + 1)]
                    for __ in range(num_hidden)]

    # 每一个输出神经元对每个隐藏神经元都有一个权重和偏倚权重
    output_layer = [[random.random() for __ in range(num_hidden + 1)]
                    for __ in range(output_size)]

    # 神经网络是从随机权重开始的
    network = [hidden_layer, output_layer]

    # 这里通过反向传播算法来训练模型
    # 10000次迭代看起来足够进行收敛
    max_iterations = 10000
    for __ in range(max_iterations):
        for input_vector, target_vector in zip(inputs, targets):
            backpropagate(network, input_vector, target_vector)

    def predict(input):
        return feed_forward(network, input)[-1]

    for i, input in enumerate(inputs):
        outputs = predict(input)
        print(i, [round(p, 2) for p in outputs])

    print([round(x, 2)
           for x in
           predict([0, 1, 1, 1, 0,
                    0, 0, 0, 1, 1,
                    0, 0, 1, 1, 0,
                    0, 0, 0, 1, 1,
                    0, 1, 1, 1, 0])])
    print()

    for neuron_idx in range(len(network[0])):
        show_weights(neuron_idx)
