import sys

input = sys.stdin.readline
N = int(input())
arr = [0 for _ in range(N)]

for i in range(N):
    arr[i]  = int(input())

print(arr)

dp = [1 for _ in range(N)]
max_value = 0

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

    if dp[i] > max_value:
        max_value = dp[i]

print(max_value)

answer = N - max_value
print(answer)