from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
g = []
q = deque()

for i in range(n):
    g.append(list(map(int, input().split())))
    for j in range(m):
        if g[i][j] == 1:
            q.append((i, j))

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and g[ny][nx] == 0:
            g[ny][nx] = g[y][x] + 1
            q.append((ny, nx))

for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            print(-1)
            exit()

print(max(map(max, g)) - 1)