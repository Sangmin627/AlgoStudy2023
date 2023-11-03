def solution_kruskal(n, costs):
    answer = 0
    parent = [i for i in range(n)]

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a,b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    edges = []
    for s,e,c in costs:
        edges.append((c,s,e))
    edges.sort()

    for edge in edges:
        cost, s, e = edge
        if find(s) != find(e):
            union(s,e)
            answer += cost

    return answer

import heapq
def solution_prim(n, costs):
    answer = 0
    q = []
    visited = [0] * n
    edges = [[] for _ in range(n)]

    heapq.heappush(q, (0, 0))  # cost, start

    for s, e, c in costs:
        edges[s].append((c, e))
        edges[e].append((c, s))

    cnt = 0
    while cnt < n:
        c, s = heapq.heappop(q)
        if visited[s]:
            continue

        visited[s] = 1
        answer += c
        cnt += 1
        for nc, ns in edges[s]:
            heapq.heappush(q, (nc, ns))

    return answer