from collections import deque

n, m, start = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visitedDfs = [0 for _ in range(n+1)]
visitedBfs = [0 for _ in range(n+1)]

def dfs(start):
    visitedDfs[start] = 1
    print(start, end=' ')
    for i in range(1, n+1):
        if graph[start][i] == 1 and visitedDfs[i] == 0:
            dfs(i)

def bfs(start):
    print()
    q = deque([start])
    visitedBfs[start] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if graph[v][i] == 1 and visitedBfs[i] == 0:
                q.append(i)
                visitedBfs[i] = 1

dfs(start)
bfs(start)