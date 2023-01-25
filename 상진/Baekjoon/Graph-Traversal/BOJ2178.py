import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n,m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(startX, startY):
    q = deque()
    q.append((startX, startY))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

bfs(0,0)
print(graph[n-1][m-1])