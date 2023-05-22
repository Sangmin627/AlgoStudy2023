from collections import deque
import sys
input = sys.stdin.readline

# 오-위-왼-아
dy = [0,1,0,-1]
dx = [1,0,-1,0]

N,M = map(int, input().split())
g = []
wall = []
for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(M):
        if g[i][j] == 1:
            wall.append((i,j))
H,W,SR,SC,FR,FC = map(int, input().split())

movable = [[0] * M for _ in range(N)]

def init_movable(ey,ex):
    if ey + 1 >= H:
        sy = ey + 1 - H
    else:
        sy = 0

    if ex + 1 >= W:
        sx = ex + 1 - W
    else:
        sx = 0

    for i in range(sy, ey+1):
        for j in range(sx, ex+1):
            movable[i][j] = -1

for y,x in wall:
    init_movable(y,x)

visited = [[-1] * M for _ in range(N)]

q = deque()
q.append((SR-1,SC-1))
visited[SR-1][SC-1] = 0
while q:
    y,x = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < N-H+1 and 0 <= nx < M-W+1:
            if visited[ny][nx] == -1 and movable[ny][nx] != -1:
                q.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1

print(visited[FR-1][FC-1])