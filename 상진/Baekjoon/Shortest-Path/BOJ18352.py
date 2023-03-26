import sys,heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
INF = int(1e9)
g = [[] for _ in range(N+1)]
dis = [INF] * (N+1)
dis[X] = 0

for _ in range(M):
    s,e = map(int, input().split())
    g[s].append((e,1)) # (노드, 거리 순)

ans = []
q = []
heapq.heappush(q, (0,X)) # heapq (거리, 노드)순

while q:
    dist, now = heapq.heappop(q)
    if dist == K:
        ans.append(now)
        continue
    if dis[now] < dist:
        continue
    for next in g[now]:
        n,c = next[0], next[1]
        cost = dist + c
        if cost < dis[n]:
            dis[n] = cost
            heapq.heappush(q, (cost, n))

if len(ans) == 0:
    print(-1)
else:
    print(*sorted(ans), sep="\n")