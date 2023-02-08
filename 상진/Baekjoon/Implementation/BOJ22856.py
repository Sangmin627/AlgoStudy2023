import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
tree = [[] * (n+1) for _ in range(n+1)]
parent = [0] * (n+1)

last_to_root_distance = 0
total_distance = 0
last_node = 0
is_right_child = [0] * (n+1)

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def in_order(node):
    global last_node, total_distance
    if node != tree[1]:
        total_distance += 1
    if node.left != -1:
        in_order(tree[node.left])
    last_node = node.data
    if node.right != -1:
        in_order(tree[node.right])

def count_distance(last_node):
    global last_to_root_distance
    if last_node == 1:
        return
    last_to_root_distance += 1
    count_distance(parent[last_node])

for i in range(n):
    data, left, right = map(int, input().split())
    if left != -1:
        parent[left] = data
    if right != -1:
        parent[right] = data
        is_right_child[right] = 1
    tree[data] = Node(data, left, right)

in_order(tree[1])
count_distance(last_node)

if last_to_root_distance == 1:
    # 마지막 노드가 오른쪽 자식 노드인 경우
    if is_right_child[last_node]:
        print(total_distance * 2 - last_to_root_distance)
    else:
        print(total_distance * 2)
else:
    print(total_distance * 2 - last_to_root_distance)
