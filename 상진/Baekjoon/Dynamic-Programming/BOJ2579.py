import sys
input = sys.stdin.readline

n = int(input())
scores = [0] + [int(input()) for _ in range(n)]
memo = [0] * 301

if n == 1:
    print(scores[1])
    exit()
elif n == 2:
    print(scores[1] + scores[2])
    exit()

memo[1] = scores[1]
memo[2] = scores[1] + scores[2]

for i in range(3, n+1):
    memo[i] = max(memo[i-3] + scores[i-1] + scores[i], memo[i-2] + scores[i])

print(memo[n])