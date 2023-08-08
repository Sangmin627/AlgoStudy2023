import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
memo = [[0] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            memo[i][j] = arr[i][j]
            ans = 1

if N == 1 or M == 1:
    print(ans)

else:
    for i in range(1,N):
        for j in range(1,M):
            if arr[i][j] == 1:
                memo[i][j] = min(memo[i-1][j-1], memo[i][j-1], memo[i-1][j]) + 1
                ans = max(ans, memo[i][j])
    print(ans ** 2)