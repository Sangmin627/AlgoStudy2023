import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())

network = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
print(network)

for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)

print(network)

answer = []

def bfs(start):
    q = deque()
    q.append(start)
    flag = False

    while q:
        a = q.popleft()

        for i in network[a]:
            if i != x and visited[i] == 0:     # i != x 으로 재방문 방지
                visited[i] += visited[a] + 1
                if visited[i] == k:
                    flag = True
                    answer.append(i)
                    continue
                q.append(i)

    if not flag:
        print(-1)
        exit()

bfs(x)
answer.sort()
print(*answer, sep="\n")