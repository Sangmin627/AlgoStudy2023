import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())

memo = [[1] * M for _ in range(N)]
if K == 0:
    for i in range(1, N):
        for j in range(1, M):
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    print(memo[N-1][M-1])
else:
    y = (K-1) // M
    x = (K-1) % M

    for i in range(1, y+1):
        for j in range(1, x+1):
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

    for i in range(y+1, N):
        for j in range(x+1, M):
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

    print(memo[y][x] * memo[-1][-1])

