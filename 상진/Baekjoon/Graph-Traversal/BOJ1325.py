import sys
from collections import deque
input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] * (node+1) for _ in range(node+1)]
answer = [0] * (node + 1)

for i in range(edge):
    s, e = map(int, input().split())
    graph[e].append(s)

def bfs(start):
    cnt = 0
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for next in graph[v]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1
                cnt += 1
    return cnt

for i in range(1, node+1):
    visited = [0] * (node + 1)
    answer[i] = bfs(i)


maxCount = max(answer)
for i in range(1, node+1):
    if answer[i] == maxCount:
        print(i, end=" ")
