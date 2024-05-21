import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0 for _ in range(k + 1)]
dp[0] = 1

for _ in range(n):
    won = int(input())
    for i in range(won, k + 1):
        dp[i] = dp[i] + dp[i - won]

    # print(dp)
print(dp[-1])