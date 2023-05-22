from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
g = [[0] * M for _ in range(N)]
Q = list(map(int, input().split()))
K = list(map(int, input().split()))
P = list(map(int, input().split()))

Q_pos = []
K_pos = []

qy = [1,0,-1,0,1,1,-1,-1]
qx = [0,1,0,-1,1,-1,1,-1]

kx = [-2,-1,1,2,2,1,-1,-2]
ky = [1,2,2,1,-1,-2,-2,-1]

for i in range(1,len(Q),2):
    Q_pos.append((Q[i]-1, Q[i+1]-1))
    g[Q[i]-1][Q[i+1]-1] = 1

for i in range(1, len(K), 2):
    K_pos.append((K[i]-1, K[i + 1]-1))
    g[K[i]-1][K[i+1]-1] = 2

for i in range(1, len(P), 2):
    g[P[i]-1][P[i+1]-1] = 3

def move_Q(sy,sx, idx):
    q = deque()
    q.append((sy,sx))
    while q:
        y,x = q.popleft()
        ny = y + qy[idx]
        nx = x + qx[idx]
        if 0 <= ny < N and 0 <= nx < M:
            if g[ny][nx] <= 0:
                q.append((ny,nx))
                g[ny][nx] = -1
            else:
                return

def move_K(sy,sx):
    for i in range(8):
        ny = sy + ky[i]
        nx = sx + kx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if g[ny][nx] == 0:
                g[ny][nx] = -1

for y,x in Q_pos:
    for i in range(8):
        move_Q(y,x,i)

for y,x in K_pos:
    move_K(y,x)

ans = 0
for i in range(N):
    for j in range(M):
        if g[i][j] == 0:
            ans += 1

print(ans)