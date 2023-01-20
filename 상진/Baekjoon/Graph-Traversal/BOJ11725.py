import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs(start):
    q = deque([start])
    parent[start] = -1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not parent[i]:
                parent[i] = v
                q.append(i)

bfs(1)

for i in parent[2:]:
    print(i)


