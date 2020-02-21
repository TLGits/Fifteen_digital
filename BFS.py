#-*-coding:utf-8-*-

import heapq
import copy
import time

# 初始状态
# S0 = [[11, 9, 4, 15],
#       [1, 3, 0, 12],
#       [7, 5, 8, 6],
#       [13, 2, 10, 14]]
S0 = [[5, 1, 2, 4],
      [9, 6, 3, 8],
      [13, 15, 10, 11],
      [0, 14, 7, 12]]

# 目标状态
SG = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 0]]

# 上下左右四个方向移动
MOVE = {'up': [1, 0],
        'down': [-1, 0],
        'left': [0, -1],
        'right': [0, 1]}

# OPEN表
OPEN = []

# 节点的总数
SUM_NODE_NUM = 0

# 状态节点
class State(object):
    def __init__(self, deepth=0, state=None, hash_value=None, father_node=None):
        '''
        初始化
        :参数 deepth: 从初始节点到目前节点所经过的步数
        :参数 state: 节点存储的状态 4*4的列表
        :参数 hash_value: 哈希值，用于判重
        :参数 father_node: 父节点指针
        '''
        self.deepth = deepth
        self.child = []  # 孩子节点
        self.father_node = father_node  # 父节点
        self.state = state  # 局面状态
        self.hash_value = hash_value  # 哈希值

    def __lt__(self, other):  # 用于堆的比较，返回距离最小的
        return self.deepth < other.deepth

    def __eq__(self, other):  # 相等的判断
        return self.hash_value == other.hash_value

    def __ne__(self, other):  # 不等的判断
        return not self.__eq__(other)


def generate_child(sn_node, sg_node, hash_set, open_table):
    '''
    生成子节点函数
    :参数 sn_node:  当前节点
    :参数 sg_node:  最终状态节点
    :参数 hash_set:  哈希表，用于判重
    :参数 open_table: OPEN表
    :返回: None
    '''
    if sn_node == sg_node:
        heapq.heappush(open_table, sg_node)
        print('已找到终止状态！')
        return
    for i in range(0, 4):
        for j in range(0, 4):
            if sn_node.state[i][j] != 0:
                continue
            for d in ['up', 'down', 'left', 'right']:  # 四个偏移方向
                x = i + MOVE[d][0]
                y = j + MOVE[d][1]
                if x < 0 or x >= 4 or y < 0 or y >= 4:  # 越界了
                    continue
                state = copy.deepcopy(sn_node.state)  # 复制父节点的状态
                state[i][j], state[x][y] = state[x][y], state[i][j]  # 交换位置
                h = hash(str(state))  # 哈希时要先转换成字符串
                if h in hash_set:  # 重复了
                    continue
                hash_set.add(h)  # 加入哈希表

                # 记录扩展节点的个数
                global SUM_NODE_NUM
                SUM_NODE_NUM += 1

                deepth = sn_node.deepth + 1  # 已经走的距离函数
                node = State(deepth, state, h, sn_node)  # 新建节点
                sn_node.child.append(node)  # 加入到孩子队列
                heapq.heappush(open_table, node)  # 加入到堆中

                # show_block(state, deepth) # 打印每一步的搜索过程


def show_block(block, step):
    print("------", step, "--------")
    for b in block:
        print(b)

def print_path(node):
    '''
    输出路径
    :参数 node: 最终的节点
    :返回: None
    '''
    print("最终搜索路径为：")
    steps = node.deepth

    stack = []  # 模拟栈
    while node.father_node is not None:
        stack.append(node.state)
        node = node.father_node
    stack.append(node.state)
    step = 0
    while len(stack) != 0:
        t = stack.pop()
        show_block(t, step)
        step += 1
    return steps


def A_start(start, end, generate_child_fn):
    '''
    A*算法
    :参数 start: 起始状态
    :参数 end: 终止状态
    :参数 generate_child_fn: 产生孩子节点的函数
    :返回: 最优路径长度
    '''
    root = State(0, start, hash(str(S0)), None)  # 根节点
    end_state = State(0, end, hash(str(SG)), None)  # 最后的节点
    if root == end_state:
        print("start == end !")

    OPEN.append(root)
    heapq.heapify(OPEN)

    node_hash_set = set()  # 存储节点的哈希值
    node_hash_set.add(root.hash_value)
    while len(OPEN) != 0:
        top = heapq.heappop(OPEN)
        if top == end_state:  # 结束后直接输出路径
            return print_path(top)
        # 产生孩子节点，孩子节点加入OPEN表
        generate_child_fn(sn_node=top, sg_node=end_state, hash_set=node_hash_set,
                          open_table=OPEN)
    print("无搜索路径!")  # 没有路径
    return -1

if __name__ == '__main__':

    time1 = time.time()
    length = A_start(S0, SG, generate_child)
    time2 = time.time()
    if length != -1:
        print("搜索最优路径长度为", length)
        print("搜索时长为", (time2 - time1), "s")
        print("共检测节点数为", SUM_NODE_NUM)


