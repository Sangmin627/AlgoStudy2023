import sys

input = sys.stdin.readline
n, t = map(int, input().split())
danwon = [[int(x) for x in input().split()] for _ in range(n)]

print(danwon)
danwon.sort()

dp = [0] * (t + 1)

for k, s in danwon:
    if k == danwon[-1][0]:
        dp[t] = max(dp[t], dp[t - k] + s)

    for j in range(t, k - 1, -1):
        dp[j] = max(dp[j], dp[j - k] + s)

# dp = [[0] * (t + 1) for _ in range(n + 1)]
# print(dp)
#
# for i in range(n):
#     k = danwon[i][0]
#     s = danwon[i][1]
#     for j in range(t + 1):
#         if j < k:
#             dp[i + 1][j] = dp[i][j]
#         else:
#             dp[i + 1][j] = max(dp[i][j], dp[i][j - k] + s)

print(dp)
print(dp[-1])