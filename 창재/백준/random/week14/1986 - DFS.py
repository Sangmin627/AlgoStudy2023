import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

input = sys.stdin.readline
n, m = map(int, input().split())
QUEEN = list(map(int, input().split()))
KNIGHT = list(map(int, input().split()))
PAWN = list(map(int, input().split()))
chess = [[0] * m for _ in range(n)]

# 체스판에 Q, K, P 위치 시키기
def init(arr, s):
    for i in range(1, arr[0] + 1):
        x = arr[i * 2 - 1]
        y = arr[i * 2]
        chess[x - 1][y - 1] = s

init(QUEEN, "Q")
init(KNIGHT, "K")
init(PAWN, "P")

for i in range(n):
    print(*chess[i])
print()

# Queen 이 갈수 있는 곳 + 1
qx = [-1, -1, -1, 0, 0, 1, 1, 1]
qy = [-1, 0, 1, -1, 1, -1, 0, 1]
def Q_dfs(x, y, i):
    nx = x + qx[i]
    ny = y + qy[i]
    if 0 <= nx < n and 0 <= ny < m:
        if chess[nx][ny] not in ["K", "Q", "P"]:
            chess[nx][ny] += 1
            Q_dfs(nx, ny, i)

# Queen 별로 실행
for q in range(1, QUEEN[0] + 1):
    for i in range(8):
        Q_dfs(QUEEN[q * 2 - 1] - 1, QUEEN[q * 2] - 1, i)    # 인덱스가 0부터 시작이니 -1 씩 해줌.

for i in range(n):
    print(*chess[i])
print()

# Knight 이 갈수 있는 곳 + 1
kx = [-2, -1, 1, 2, 2, 1, -1, -2]
ky = [-1, -2, -2, -1, 1, 2, 2, 1]
def K_dfs(x, y, i):
    nx = x + kx[i]
    ny = y + ky[i]
    if 0 <= nx < n and 0 <= ny < m:
        if chess[nx][ny] not in ["K", "Q", "P"]:
            chess[nx][ny] += 1

# Knight 별로 실행
for k in range(1, KNIGHT[0] + 1):
    for i in range(8):
        K_dfs(KNIGHT[k * 2 - 1] - 1, KNIGHT[k * 2] - 1, i)  # 인덱스가 0부터 시작이니 -1 씩 해줌.

for i in range(n):
    print(*chess[i])
print()

# 마지막 0(안전한 곳) 개수 세기
answer = 0
for i in range(n):
    answer += chess[i].count(0)

print(answer)