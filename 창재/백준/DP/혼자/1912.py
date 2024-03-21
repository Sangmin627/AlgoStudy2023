import sys

input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = S[0]

for i in range(1, N):
    dp[i] = max(dp[i - 1] + S[i], S[i])

# print(dp)
print(max(dp))