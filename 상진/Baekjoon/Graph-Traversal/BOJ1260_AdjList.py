from collections import deque

n, m, start = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]

visitedDfs = [0 for _ in range(n+1)]
visitedBfs = [0 for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    graph[i].sort()

def dfs(start):
    visitedDfs[start] = 1
    print(start, end=' ')
    for i in graph[start]:
        if not visitedDfs[i]:
            dfs(i)

def bfs(start):
    print()
    q = deque([start])
    visitedBfs[start] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visitedBfs[i]:
                q.append(i)
                visitedBfs[i] = 1

dfs(start)
bfs(start)