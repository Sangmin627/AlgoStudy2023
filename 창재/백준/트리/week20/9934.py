from collections import deque

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def pre_input(x, order):
    if tree[x].left_node is not None:
        pre_input(tree[x].left_node, order)

    real_data = order.pop()
    tree[x].data = real_data

    if tree[x].right_node is not None:
        pre_input(tree[x].right_node, order)


K = int(input())
order = list(map(int, input().split()))
tree = {}

# 초기화 : 높이 K 만큼의 트리 만들기
for i in range(2 ** K - 1):
    if i < 2 ** (K - 1) - 1: # K - 1 층까지
        tree[i] = Node(i, 2 * i + 1, 2 * i + 2)
    else: # K 층
        tree[i] = Node(i, None, None)


order.reverse() # pop해서 left 부터 채우기 위해.
pre_input(0, order)


for i in range(1, K + 1):
    for j in range(2 ** (i - 1) - 1, 2 ** i - 1):
        print(tree[j].data, end=" ")
    print()