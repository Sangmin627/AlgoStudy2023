import sys

input = sys.stdin.readline
N = int(input())
T = [0 for _ in range(N + 1)]
P = [0 for _ in range(N + 1)]
dp = [0 for _ in range(N + 2)]

for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

if T[N] == 1:
    dp[N] = P[N]

maxValue = dp[N]
for i in range(N-1, 0, -1):
    next = i + T[i]
    print("next = ", next)

    if next <= N:
        dp[i] = max(dp[next] + P[i], maxValue)
        maxValue = dp[i]
    elif next - 1 == N:
        dp[i] = max(P[i], maxValue)
        maxValue = dp[i]
    else:
        dp[i] = maxValue

    print("dp[", i, "] = ", dp[i])


print(dp)
print(dp[1])