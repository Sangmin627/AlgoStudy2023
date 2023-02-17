import sys
from collections import deque

def print2D(arr):
    for i in range(len(box)):
        print(box[i])

# 입력 받기
input = sys.stdin.readline
M, N = map(int, input().split())

box = [0] * N

for i in range(N):
    box[i] = list(map(int, input().split()))

print2D(box)


# BFS 를 위해 queue 초기화
q = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:  # 맨 처음 1인 애들 queue 에 담음
            q.append((i, j))

print(q)

count = 0   # 일수 count
nx = [0, 1, 0, -1]
ny = [-1, 0, 1, 0]

# 한번에(=하루에) 다 담을 수 있는 애들 다 담고 count를 위해 check
q.append(("check", "check"))
while q:
    x, y = q.popleft()
    if x == "check":
        if not q:
            break
        else:
            count += 1
            q.append(("check", "check"))

    else:
        for i in range(4):
            dx = x - nx[i]
            dy = y - ny[i]
            if 0 <= dx < N and 0 <= dy < M:
                if box[dx][dy] == 0:
                    box[dx][dy] = 1
                    q.append((dx, dy))

print2D(box)

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            sys.exit()

print(count)