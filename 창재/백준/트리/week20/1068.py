import sys


class Node:
    def __init__(self, data, parent_node):
        self.data = data
        self.parent_node = parent_node
        self.child_node = []

    def add(self, child_node):
        self.child_node.append(child_node)


def count_leaf(x):
    global count

    if not tree[x].child_node:
        count += 1
        return

    for c in tree[x].child_node:
        count_leaf(c)

def delete(d):
    p = tree[d].parent_node

    if p is None:
        print(0)
        sys.exit()

    tree[p].child_node.remove(d)


input = sys.stdin.readline

N = int(input())
tree = {}
root = -1
count = 0

# 트리 초기화
for i in range(N):
    tree[i] = Node(i, None)

parents_info = list(map(int, input().split()))
for idx, p in enumerate(parents_info):
    if p == -1:
        root = idx
        continue

    tree[idx].parent_node = p
    tree[p].child_node.append(idx)

# 노드 삭제
D = int(input())
delete(D)

# 리프 노드 개수 count
count_leaf(root)
print(count)