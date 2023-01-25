n = int(input())
pairCount = int(input())

graph = [[0] * n for _ in range(n)]
visited = [0 for _ in range(n)]

for i in range(pairCount):
    x,y = map(int, input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

def dfs(start):
    visited[start] = 1
    for i in range(n):
        if graph[start][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(0)
print(sum(visited[1:]))

