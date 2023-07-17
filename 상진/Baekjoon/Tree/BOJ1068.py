import sys
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
tree = [[] for _ in range(N)]
root_node = 0
for i in range(N):
    p = parents[i]
    if p == -1:
        root_node = i
        continue
    tree[p].append(i)

delete_node = int(input())

def dfs(node):
    global ans
    if delete_node in tree[node]:
        tree[node].remove(delete_node)
    if not tree[node]:
        ans += 1
    for i in tree[node]:
        dfs(i)

ans = 0
if delete_node == root_node:
    print(0)
else:
    dfs(root_node)
    print(ans)

