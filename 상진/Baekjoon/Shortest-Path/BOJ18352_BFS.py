from collections import deque
import sys
input = sys.stdin.readline

node,edge,dis,start = map(int, input().split())
g = [[] for _ in range(node+1)]

for i in range(edge):
    s,e = map(int, input().split())
    g[s].append(e)

ans = []
visited = [-1] * (node+1)
q = deque()
q.append(start)
visited[start] = 0

while q:
    now = q.popleft()
    if visited[now] == dis:
        ans.append(now)
    for next in g[now]:
        if visited[next] == -1:
            visited[next] = visited[now] + 1
            q.append(next)

if len(ans) == 0:
    print(-1)
else:
    print(*sorted(ans), sep="\n")