from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]

loops = min(N,M) // 2
for i in range(loops):
    cycle = (((N-i*2) - 1) + ((M-i*2) - 1)) * 2 # cycle만큼 돌면 제자리
    q = deque()
    q.extend(g[i][i:M-i]) # 위
    for r in range(i+1, N-1-i): # 오른쪽
        q.append(g[r][M-i-1])
    q.extend(g[N-i-1][i:M-i][::-1]) # 아래
    for r in range(N-2-i, i, -1): # 왼쪽
        q.append(g[r][i])

    q.rotate(-(R % cycle))

    for j in range(i, M-i): # 위
        g[i][j] = q.popleft()
    for j in range(i+1, N-1-i): # 오른쪽
        g[j][M-i-1] = q.popleft()
    for j in range(M-i-1, i-1, -1): # 아래
        g[N-i-1][j] = q.popleft()
    for j in range(N-2-i, i, -1): # 왼쪽
        g[j][i] = q.popleft()

for i in range(N):
    print(*g[i])
