import sys
from collections import deque


def bfs(start):
    count = 0

    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                count += 1

    return count


if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    cnt = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[b].append(a)

    print(graph)

    for i in range(1, N + 1):
        visited = [0] * (N + 1)
        cnt[i] = bfs(i)

    print(cnt)

    max = max(cnt)
    for i in range(1, N + 1):
        if cnt[i] == max:
            print(i, end=' ')


