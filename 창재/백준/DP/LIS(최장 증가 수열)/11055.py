import copy
import sys

input = sys.stdin.readline
N = int(input())

sequence = list(map(int, input().split()))
dp = copy.deepcopy(sequence)

# solution1
# for i in range(N):
#     for j in range(i + 1, N):
#         if sequence[i] < sequence[j]:
#             dp[j] = max(dp[j], dp[i] + sequence[j])

#solution2
for i in range(N):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j] + sequence[i])

print(sequence)
print(dp)

print(max(dp))