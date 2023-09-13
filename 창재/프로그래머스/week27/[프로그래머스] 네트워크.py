def dfs(n, computers, memo, x, count):
    for j in range(n):
        if memo[j] == -1 and computers[x][j] == 1:
            memo[j] = count
            dfs(n, computers, memo, j, count)

def solution(n, computers):
    memo = [-1] * n
    count = 1

    for i in range(n):
        if memo[i] == -1:
            memo[i] = count
            dfs(n, computers, memo, i, count)
            print("memo = ", memo)
            count += 1

    return count - 1