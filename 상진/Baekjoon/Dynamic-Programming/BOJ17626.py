n = int(input())

dp = [4] * (n+1)
dp[1] = 1

for i in range(2, int(n ** 0.5) + 1):
    dp[i**2] = 1

for i in range(1, n+1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i - (j ** 2)] + 1, dp[i])

print(dp[n])