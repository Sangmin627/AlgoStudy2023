import sys
from collections import deque


def dfs(network, start, visited):
    visited[start] = True
    print(start, end=' ')

    network[start].sort()   # 정점 번호가 작은거 부터 하기 위해
    for i in network[start]:
        if not visited[i]:
            dfs(network, i, visited)


def bfs(network, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        network[v].sort()   # 정점 번호가 작은거 부터 하기 위해
        for i in network[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, start = map(int, input().split())

    # 헷갈렸음. 노드의 갯수만큼 만들어야 하니까, M이 아니라 N으로 해야댐!
    network = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for i in range(M):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)

    # DFS
    dfs(network, start, visited)

    print()
    visited = [False] * (N + 1) # 초기화
    # BFS
    bfs(network, start, visited)