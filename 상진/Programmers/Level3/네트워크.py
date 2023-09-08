def solution(n, computers):
    visited = [0] * n

    def dfs(start, cnt):
        visited[start] = cnt
        for i in range(n):
            if i != start and computers[start][i] == 1:
                if not visited[i]:
                    visited[i] = cnt
                    dfs(i, cnt)

    cnt = 0
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i, cnt)
    return cnt