import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
g = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    relationships = " " + input().rstrip()
    for j in range(1,N+1):
        if relationships[j] == "Y":
            g[i][j] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j:
                continue
            if g[i][j] == 1 or (g[i][k] == 1 and g[k][j] == 1):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

ans = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if 0 < g[i][j] <= 2:
            cnt += 1
    ans = max(ans, cnt)
print(ans)