# L : 잃을 체력
# J : 얻을 기쁨
# 0 또는 음수이면 죽음. -> 무조건 1 이상 이어야 함.
# 최대 기쁨 출력
# dp[][] : 가로 -> 생명, 세로 -> 기쁨

import sys

input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [0 for _ in range(100)]

p = [i for i in range(100)]
print(*p)

for i in range(N):
    for j in range(99, L[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])
    print(*dp)

print(max(dp))