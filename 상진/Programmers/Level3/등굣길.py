def solution(m, n, puddles):
    memo = [[0] * m for _ in range(n)]

    for x, y in puddles:
        memo[y - 1][x - 1] = -1

    for i in range(n):
        if memo[i][0] == -1:
            break
        memo[i][0] = 1

    for i in range(m):
        if memo[0][i] == -1:
            break
        memo[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            if memo[i][j] == 0:
                up = memo[i-1][j] if memo[i-1][j] != -1 else 0
                left = memo[i][j-1] if memo[i][j-1] != -1 else 0
                memo[i][j] = up+left % 1000000007

    return memo[-1][-1] % 1000000007