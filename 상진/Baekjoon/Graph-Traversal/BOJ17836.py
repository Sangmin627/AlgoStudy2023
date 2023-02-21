from collections import deque
import sys
input = sys.stdin.readline

dy = [-1,0,1,0]
dx = [0,-1,0,1]

N,M,T = map(int, input().split())
g = []
for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(M):
        if g[i][j] == 2:
            gram_y, gram_x = i, j

visited = [[-1] * M for _ in range(N)]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == -1:
                if g[ny][nx] != 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

bfs()
start_to_princess = visited[N-1][M-1]
start_to_gram = visited[gram_y][gram_x]

if start_to_gram == -1 and start_to_princess == -1:
    print("Fail")
else:
    if start_to_gram != -1:
        gram_to_princess = (N - 1 - gram_y) + (M - 1 - gram_x)
        start_to_gram_to_princess = start_to_gram + gram_to_princess
        if start_to_princess != -1:
            answer = min(start_to_princess, start_to_gram_to_princess)
        else:
            answer = start_to_gram_to_princess
    if answer > T:
        print("Fail")
    else:
        print(answer)