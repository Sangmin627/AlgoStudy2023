import sys

input = sys.stdin.readline
N, M, H = map(int, input().split())

arr = [0 for _ in range(N)]
dp = [0 for _ in range(H + 1)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

# print(arr)

dp[0] = 1
for a in arr:
    memo = [0 for _ in range(H + 1)]
    for v in a:
        for i in range(v, H + 1):
            memo[i] += dp[i - v]

    for j in range(H + 1):
        dp[j] += memo[j]

# print(dp)
# print(dp[H])
print(dp[H]%10007)