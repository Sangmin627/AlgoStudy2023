import sys
input = sys.stdin.readline

N,T = map(int, input().split())
ts = [[0,0]]

for i in range(N):
    K,S = map(int, input().split())
    ts.append([K,S])

memo = [[0] * (T+1) for _ in range(N+1)]

for i in range(1,N+1):
    t,s = ts[i]
    for j in range(1,T+1):
        if j < t:
            memo[i][j] = memo[i-1][j]
        else:
            memo[i][j] = max(memo[i-1][j-t] + s, memo[i-1][j])

print(memo[-1][-1])
