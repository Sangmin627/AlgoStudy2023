import sys
input = sys.stdin.readline

N,M = map(int, input().split())

g = [[] * (N+1) for _ in range(N+1)]
for i in range(M):
    s,e = map(int, input().split())
    g[e].append(s)

memo = [0] * (N+1)
for i in range(1, N+1):
    if not g[i]:
        memo[i] = 1
        continue
    for p in g[i]:
        memo[i] = max(memo[p] + 1, memo[i])

for i in memo[1:]:
    print(i, end=" ")

