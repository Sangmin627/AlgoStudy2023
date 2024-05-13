import sys

input = sys.stdin.readline

while 1:
    N = int(input())
    if N == 0:
        break

    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        dp[0][i] = 1

    for i in range(1, N + 1):
        for j in range(N + 1 - i):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j + 1]

    print(dp[N][0])