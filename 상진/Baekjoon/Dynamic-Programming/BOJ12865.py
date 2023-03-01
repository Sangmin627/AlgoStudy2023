import sys
input = sys.stdin.readline

N,K = map(int, input().split())

WV = [(0,0)]
for _ in range(N):
    w,v = map(int, input().split())
    WV.append((w,v))

memo = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1):
    w,v = WV[i][0], WV[i][1]
    for j in range(1,K+1):
        if j >= w:
            memo[i][j] = max(memo[i-1][j], memo[i-1][j-w] + v)
        else:
            memo[i][j] = memo[i-1][j]

print(memo[N][K])

