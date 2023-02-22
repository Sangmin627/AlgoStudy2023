from collections import deque
import sys
input = sys.stdin.readline

dh = [-1,1]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N, H = map(int, input().split())
g = [[] for _ in range(H)]
q = deque()

for k in range(H):
    for i in range(N):
        g[k].append(list(map(int, input().split())))
        for j in range(M):
            if g[k][i][j] == 1:
                q.append((k, i, j))

while q:
    h, y, x = q.popleft()
    for i in range(2):
        nh = h + dh[i]
        if 0 <= nh < H:
            if g[nh][y][x] == 0:
                g[nh][y][x] = g[h][y][x] + 1
                q.append((nh, y, x))
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= ny < N and 0 <= nx < M:
            if g[h][ny][nx] == 0:
                g[h][ny][nx] = g[h][y][x] + 1
                q.append((h, ny, nx))

answer = -1
for k in range(H):
    for i in range(N):
        for j in range(M):
            if g[k][i][j] == 0:
                print(-1)
                exit()
            answer = max(answer, g[k][i][j])

print(answer-1)