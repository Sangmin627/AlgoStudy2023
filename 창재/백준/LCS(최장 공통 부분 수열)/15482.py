import sys

input = sys.stdin.readline
S1 = input()
S2 = input()

L1 = len(S1)
L2 = len(S2)

dp = [[0 for _ in range(L1 + 1)] for _ in range(L2 + 1)]

for i in range(1, L2 + 1):
    for j in range(1, L1 + 1):
        if S2[i - 1] == S1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

for d in dp:
    print(*d)
print()

print(dp[-1][-1])