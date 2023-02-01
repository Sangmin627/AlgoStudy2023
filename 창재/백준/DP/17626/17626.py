import sys

n = int(sys.stdin.readline())

dp = [0, 1]

for i in range(2, n + 1):
    min_value = 4
    r = 1

    while r**2 <= i:
        min_value = min(min_value, dp[i - r**2])
        r += 1

    dp.append(min_value + 1)

print(dp[n])