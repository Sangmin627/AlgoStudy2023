import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    def bfs(sx, sy):
        q = deque()
        q.append([sx, sy])

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 1:
                        q.append([nx, ny])
                        arr[nx][ny] = 0


    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)