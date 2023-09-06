# class Node:
#     def __init__(self, data, parent_node):
#         self.data = data
#         self.parent_node = parent_node
#         self.child_node = []
import sys

input  = sys.stdin.readline
N = int(input())

# tree = [[] for _ in range(N + 1)]
tree = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    # tree[a].append(b)
    # tree[b].append(a)
    tree[a] += 1
    tree[b] += 1

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())

    if t == 1:
        # if len(tree[k]) >= 2:
        if tree[k] >= 2:
            print("yes")
        else:
            print("no")
    else:
        print("yes")

# tree = {}

# for i in range(1, N + 1):
#     tree[i] = Node(i, None)
#
# for i in range(N - 1):
#     a, b = map(int, input().split())
#     tree[a].child_node.append(b)
#     tree[b].parent_node = a
#
# q = int(input())
# for _ in range(q):
#     t, k = map(int, input().split())
#
#     if t == 1:
#         if tree[k].child_node:
#             if tree[k].parent_node is None: # 루트 노드
#                 if len(tree[k].child_node) >= 2: # 루트 노드, 자식 2이상
#                     print("yes")
#                 else: # 루트 노드, 자식이 1개
#                     print("no")
#             else: # 루트노드도 아니고 리프 노드도 아닌 노드.
#                 print("yes")
#         else: # 리프 노드.
#             print("no")
#
#     else:
#         print("yes")