from collections import deque

def bfs(start, network, visited):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        x = q.popleft()

        for i in network[x]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[x] + 1

def solution(n, edge):
    edge.sort(key=lambda e: (e[0], e[1]))

    network = [[] for _ in range(n + 1)]
    visited = [-1 for _ in range(n + 1)]

    for e in edge:
        x, y = e[0], e[1]

        network[x].append(y)
        network[y].append(x)

    bfs(1, network, visited)

    return visited.count(max(visited))