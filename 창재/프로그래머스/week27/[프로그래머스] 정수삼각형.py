def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(0, i + 1):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
            elif j == i:
                triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i - 1][j - 1], triangle[i - 1][j])

    return max(triangle[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))