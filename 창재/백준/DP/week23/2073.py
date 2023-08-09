import sys

input = sys.stdin.readline
D, P = map(int, input().split())
INF = 10e9
L = [0 for _ in range(P)]
C = [0 for _ in range(P)]

for i in range(P):
    L[i], C[i] = map(int, input().split())

dp = [0 for _ in range(D + 1)]

dp[0] = INF
for i in range(P):
    for j in range(D, L[i] - 1, -1):
        if dp[j] == INF:
            dp[j] = min(dp[j], min(dp[j - L[i]], C[i]))
        else:
            dp[j] = max(dp[j], min(dp[j - L[i]], C[i]))

        if i == P - 1:
            break


print(dp[D])