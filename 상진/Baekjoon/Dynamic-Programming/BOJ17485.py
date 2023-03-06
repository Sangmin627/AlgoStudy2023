import sys
input = sys.stdin.readline

N,M = map(int, input().split())
INF = int(1e9)
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

memo = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

for i in range(M):
    for j in range(3):
        memo[0][i][j] = arr[0][i]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            if k == 0:
                if j + 1 < M:
                    memo[i][j][0] = min(memo[i-1][j+1][1], memo[i-1][j+1][2]) + arr[i][j]
            if k == 1:
                memo[i][j][1] = min(memo[i-1][j][0] , memo[i-1][j][2]) + arr[i][j]
            if k == 2:
                if j - 1 >= 0:
                    memo[i][j][2] = min(memo[i-1][j-1][0], memo[i-1][j-1][1]) + arr[i][j]

ans = memo[-1]
print(min(map(min, ans)))