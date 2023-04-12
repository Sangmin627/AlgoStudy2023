import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
kx, ky = map(int, input().split())

chess = [[0] * n for _ in range(n)]
E = []
for _ in range(m):
    x, y = map(int, input().split())
    E.append((x-1, y-1))

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(sx, sy, m):
    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if chess[nx][ny] == 0:
                    chess[nx][ny] = chess[x][y] + 1
                    q.append((nx, ny))
                    # if (nx, ny) in E: --> in : O(n) 의 시간 복잡도를 가짐
                    #     m -= 1

        # if m <= 0:
        #     break


bfs(kx-1, ky-1, m)
print(chess)
for i in range(m):
    x, y = E[i]
    print(chess[x][y], end=" ")