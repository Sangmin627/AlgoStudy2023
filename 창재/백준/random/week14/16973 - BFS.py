import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0] for _ in range(n + 1)]
visited = [[-1] * (m + 1) for _ in range(n + 1)]

arr[0] += [0] * m
for i in range(1, n + 1):
    arr[i] += list(map(int, input().split()))

h, w, s_r, s_c, f_r, f_c = map(int, input().split())

wall = []
for i in range(n + 1):
    for j in range(m + 1):
        if arr[i][j] == 1:
            wall.append([i, j])

for wa in wall:
    i, j = wa[0], wa[1]
    for a in range(1, h):
        if 0 < i - a:
            arr[i - a][j] = "x"
            if 0 < j - (w - 1):
                arr[i - a][j - (w - 1)] = "x"
    for b in range(1, w):
        if 0 < j - b:
            arr[i][j - b] = "x"
            if 0 < i - (h - 1):
                arr[i - (h - 1)][j - b] = "x"


for i in range(n + 1):
    print(*arr[i])
print()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
arr[s_r][s_c] = - 1  # 시작점을 다시 탐색하지 않게 하기 위해

for i in range(n + 1):
    print(*arr[i])
print()

def bfs():
    q = deque()
    q.append((s_r, s_c))
    visited[s_r][s_c] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx <= (n - h + 1) and 0 < ny <= (m - w + 1):
                if arr[nx][ny] == 0 and visited[nx][ny] == -1:
                    # arr[nx][ny] = arr[x][y] - 1
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

        for i in range(n + 1):
            print(*arr[i])
        print()


bfs()

for i in range(n + 1):
    print(*arr[i])
print()

for i in range(n + 1):
    print(*visited[i])
print()

print(-arr[f_r][f_c] - 1)
print(visited[f_r][f_c])