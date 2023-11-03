from collections import deque

def solution(n, edge):
    g = [[] for _ in range(n + 1)]

    for s, e in edge:
        g[s].append(e)
        g[e].append(s)

    visited = [-1] * (n + 1)
    q = deque()
    q.append(1)
    visited[1] = 0
    while q:
        now = q.popleft()
        for i in g[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)

    max_val = max(visited)
    answer = visited.count(max_val)
    return answer
