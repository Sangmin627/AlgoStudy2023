import sys
from collections import deque

def bfs(tree, root, parents):
    queue = deque([root])
    visited[root] = True

    while queue:
        v = queue.popleft()
        for i in tree[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                parents[i] = v


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    tree = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    parents = [0] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    bfs(tree, 1, parents)

    for i in range(2, N + 1):
        print(parents[i])