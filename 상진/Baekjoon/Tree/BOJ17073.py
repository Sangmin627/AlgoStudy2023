import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N,W = map(int, input().split())
leaf_node = 0
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(node):
    global leaf_node
    is_leaf_node = True
    for i in tree[node]:
        if not visited[i]:
            is_leaf_node = False
            visited[i] = 1
            dfs(i)
    else:
        if is_leaf_node:
            leaf_node += 1
            return

visited[1] = 1
dfs(1)
print(W / leaf_node)
