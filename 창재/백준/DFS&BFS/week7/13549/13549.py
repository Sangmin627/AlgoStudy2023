import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
LIMIT = 100001
if K <= N:
    print(N - K)
else:
    q = deque()
    q.append(N)

    INF = 10e9
    visited = [INF for _ in range(LIMIT + 1)]

    visited[N] = 0
    while q:
        x = q.popleft()

        if 0 <= 2 * x <= LIMIT and (visited[x] < visited[2 * x]):
            q.append(2 * x)
            visited[2 * x] = visited[x]

        if 0 <= x + 1 <= LIMIT and (visited[x] + 1 < visited[x + 1]):
            q.append(x + 1)
            visited[x + 1] = visited[x] + 1

        if 0 <= x - 1 <= LIMIT and (visited[x] + 1 < visited[x - 1]):
            q.append(x - 1)
            visited[x - 1] = visited[x] + 1

    print(visited[K])