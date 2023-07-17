import sys
limit_number = 1000000
sys.setrecursionlimit(limit_number)

def dfs(start, tree, visited):
    childs = []
    for c in tree[start]:
        if visited[c] == 0:
            childs.append(c)

    child_count = len(childs)
    if child_count == 0 :
        return

    p = visited[start] / child_count
    visited[start] = -1

    for c in childs:
        visited[c] = p
        dfs(c, tree, visited)


input = sys.stdin.readline
N, W = map(int, input().split())

tree = [[] for i in range(N + 1)]
visited = [0] * (N + 1)
visited[1] = W

for _ in range(N - 1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

dfs(1, tree, visited)

count = 0
sum_value = 0
for v in visited:
    if v > 0:
        count += 1
        sum_value += v

print(sum_value/count)