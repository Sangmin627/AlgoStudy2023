import sys
input = sys.stdin.readline

INF = int(1e9)
N,K = map(int, input().split())
coins = sorted((int(input()) for _ in range(N)))

memo = [INF] * (K+1)
memo[0] = 0

for i in range(N):
    val = coins[i]
    for j in range(val, K+1):
        if memo[j-val] != INF:
            if memo[j] != INF:
                memo[j] = min(memo[j-val] + 1, memo[j])
            else:
                memo[j] = memo[j-val] + 1

if memo[-1] == INF:
    print(-1)
else:
    print(memo[K])