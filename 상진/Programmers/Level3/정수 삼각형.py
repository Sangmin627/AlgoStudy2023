def solution(triangle):
    memo = [[0] * len(triangle[-1]) for _ in range(len(triangle))]
    memo[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                memo[i][j] = memo[i - 1][j] + triangle[i][j]
            elif j == i:
                memo[i][j] = memo[i - 1][j - 1] + triangle[i][j]
            else:
                memo[i][j] = max(memo[i - 1][j - 1], memo[i - 1][j]) + triangle[i][j]

    return max(memo[-1])