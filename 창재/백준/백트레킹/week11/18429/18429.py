# DFS다 이건.
import sys

def dfs(order, start, visited, weight):
    global cnt
    order.append(start)
    visited[start] = True
    weight += kit[start] - k

    if weight < 500:
        return

    if len(order) == n:
        print(*order)
        cnt += 1
        return

    for j in range(1, n + 1):
        if not visited[j]:  # False 이면
            dfs(order, j, visited, weight)
            order.pop()
            visited[j] = False


input = sys.stdin.readline
n, k = map(int, input().split())
kit = [0]
kit += list(map(int, input().split()))
print(kit)

cnt = 0
for i in range(1, n + 1):
    order = []
    visited = [False] * (n + 1)
    weight = 500
    dfs(order, i, visited, weight)

print(cnt)