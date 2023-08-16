import sys
from collections import deque

def print2D(arr):
    for i in range(H):
        for j in range(N):
            print(box[i][j])

# 입력 받기
input = sys.stdin.readline
M, N, H = map(int, input().split())

box = [[[] for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        box[i][j] = list(map(int, input().split()))

print2D(box)
print(box)


# BFS 를 위해 queue 초기화
q = deque()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 1:  # 맨 처음 1인 애들 queue 에 담음
                q.append((k, i, j))

print(q)

count = 0   # 일수 count
nx = [0, 1, 0, -1, 0, 0]
ny = [-1, 0, 1, 0, 0, 0]
nh = [0, 0, 0, 0, 1, -1]

# 한번에(=하루에) 다 담을 수 있는 애들 다 담고 count를 위해 check
q.append(("check", "check", "check"))
while q:
    h, x, y = q.popleft()
    if x == "check":
        if not q:
            break
        else:
            count += 1
            q.append(("check", "check", "check"))

    else:
        for i in range(6):
            dh = h - nh[i]
            dx = x - nx[i]
            dy = y - ny[i]
            if 0<= dh < H and 0 <= dx < N and 0 <= dy < M:
                if box[dh][dx][dy] == 0:
                    box[dh][dx][dy] = 1
                    q.append((dh, dx, dy))
#
# print2D(box)
#
for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 0:
                print(-1)
                sys.exit()
#
print(count)