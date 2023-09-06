import sys
from collections import deque


def print2(arr):
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end='\t')
        print()


input = sys.stdin.readline
N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

print2(miro)
print2(visited)
start = [0, 0]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(miro, sx, sy, visited):
    q = deque()
    q.append((sx, sy))

    visited[sx][sy] = True
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                a = miro[nx][ny]
                if miro[nx][ny] == 1:
                    q.append((nx, ny))
                    miro[nx][ny] = miro[x][y] + 1
                    visited[nx][ny] = True
        count += 1

    return count
result = bfs(miro, 0, 0, visited)
print(result)
print(miro[N-1][M-1])
print2(visited)
print2(miro)