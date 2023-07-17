"""
시간 목잡도가 O(n x 2^m) 아닌가..
"""

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
space = [[int(x) for x in input().split()] for _ in range(n)]

print(space)

dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]

print(dp)
for j in range(m):
    for k in range(3):
        dp[0][j][k] = space[0][j]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            dp[i][j][0] = max()

# dpd = [[0] * (m) for _ in range(n)]
# dpd[0] = space[0]
# print(dpd)
#
# for i in range(0, n):
#     for j in range(m):
#         dpd[i + 1][j - 1] = max(dpd[i + 1][j - 1], dpd[i][j])
#         dpd[i + 1][j] += dpd[i][j]
#         dpd[i + 1][j + 1] += dpd[i][j]