import sys
from collections import deque

input = sys.stdin.readline
N, L, R = map(int, input().split())

A = [0] * N
for i in range(N):
    A[i] = list(map(int, input().split()))

print(A)

flag = True

while flag:
    flag = False

q = deque()
q2 = deque()

q.append([0, 0])
q2.append([0, 0])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

popSum = A[0][0]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x - dx[i]
        ny = y - dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if L <= abs(A[x][y] - A[nx][ny]) <= R:
                q.append([nx, ny])
                q2.append([nx, ny])
                popSum += A[nx][ny]
                flag = True

popAvg = int(popSum / len(q2))

while q2:
    x, y = q.popleft()
    A[x][y] = popAvg