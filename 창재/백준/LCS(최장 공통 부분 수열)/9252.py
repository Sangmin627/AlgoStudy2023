import sys

input = sys.stdin.readline
S1 = list(input().rstrip())
S2 = list(input().rstrip())

L1 = len(S1)
L2 = len(S2)

dp = [[0 for _ in range(L1 + 1)] for _ in range(L2 + 1)]
memo = {}
for i in range(1, L2 + 1):
    for j in range(1, L1 + 1):
        if S2[i - 1] == S1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] not in memo:
                memo[dp[i][j]] = [(i, j)]
            else:
                memo[dp[i][j]].append((i, j))
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

for d in dp:
    print(*d)
print()

lcs = dp[-1][-1]
print(lcs)

if lcs != 0:
    x = memo[lcs][0][0]
    y = memo[lcs][0][1]

    answer = [S1[y - 1]]

    for i in range(lcs - 1, 0, -1):
        for m in memo[i]:
            if m[0] < x and m[1] < y:
                answer.append(S1[m[1] - 1])

                x = m[0]
                y = m[1]

                break


    answer.reverse()
    print(''.join(answer))