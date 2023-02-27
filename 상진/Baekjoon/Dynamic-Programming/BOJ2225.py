N, K = map(int, input().split())

memo = [[0] * (N+1) for _ in range(K+1)]

for i in range(N+1):
    memo[1][i] = 1

for i in range(1, K+1):
    memo[i][0] = 1

for i in range(1, K+1):
    for j in range(1, N+1):
        memo[i][j] = memo[i-1][j] + memo[i][j-1]

print(memo[K][N] % 1_000_000_000)