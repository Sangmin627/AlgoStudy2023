import sys

input = sys.stdin.readline

t, w = map(int, input().split())
dp = [[0 for _ in range(w + 2)] for _ in range(t + 1)]

for i in range(1, t + 1):
    tree = int(input())

    if tree == 2:
        for j in range(1, w + 2, 2):
            dp[i][j] = dp[i-1][j]

        for j in range(2, w + 2, 2):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

    else:
        for j in range(1, w + 2, 2):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

        for j in range(2, w + 2, 2):
            dp[i][j] = dp[i - 1][j]

for i in range(t + 1):
    print(*dp[i])

print(max(dp[t][:w + 2]))