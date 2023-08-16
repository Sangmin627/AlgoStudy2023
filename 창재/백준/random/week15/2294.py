import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [0] * n
for i in range(n):
    c = int(input())
    if c <= k:
        coin[i] = c

coin = list(set(coin))
print(coin)

memo = [1e9] * (k + 1)
memo[0] = 0

for c in coin:
    for i in range(c, k + 1):
        memo[i] = min(memo[i - c] + 1, memo[i])

print(memo)
if memo[k] == 1e9:
    print(-1)
else:
    print(memo[k])
