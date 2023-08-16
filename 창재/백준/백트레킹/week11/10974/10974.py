# DFS다 이건.
import sys


def dfs(order, start, visited):
    order.append(start)
    visited[start] = True

    if len(order) == N:
        print(*order)
        return

    for j in range(1, N + 1):
        if not visited[j]:  # False 이면
            dfs(order, j, visited)
            order.pop()
            visited[j] = False


input = sys.stdin.readline
N = int(input())

for i in range(1, N + 1):
    order = []
    visited = [False] * (N + 1)
    dfs(order, i, visited)