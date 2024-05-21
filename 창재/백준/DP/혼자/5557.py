import sys

# 음수는 배우지 않았다.
# 20넘는 숫자는 모른다.
# 중간에 나오는 모든 숫자가 0 <=  <= 20
input = sys.stdin.readline
N = int(input())

dp = [[0 for _ in range(21)] for _ in range(N - 1)]
numbers = list(map(int, input().split()))
value = numbers.pop()

for idx, n in enumerate(numbers):
    if idx == 0:
        dp[idx][n] = 1
        continue

    for i in range(21):
        if i >= n:
            dp[idx][i] += dp[idx - 1][i - n]
        if i <= 20 - n:
            dp[idx][i] += dp[idx - 1][i + n]

for i in range(N - 1):
    print(*dp[i])

print(dp[-1][value])