# 이렇게 하니까 시간초과가 뜨고 계산이 안됨
# import sys
# limit_number = 100000000
# sys.setrecursionlimit(limit_number)
#
# N = int(sys.stdin.readline())
#
#
# def sol(N):
#     if N == 1:
#         return 1
#     elif N == 2:
#         return 2
#     else:
#         return (sol(N - 1) + sol(N - 2))%10007
#
#
# print(sol(N) % 10007)

# 이게 훠어어어어어얼씬 빨라

import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)

for i in range(1, N + 1):
    if i <= 2:
        dp[i] = i
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N] % 10007)
