import sys
input = sys.stdin.readline

MONEY = int(input())
N = int(input())
coins = [[0,0]]
memo = [[0] * (MONEY+1) for _ in range(N+1)]

for i in range(N):
    p,n = map(int, input().split())
    coins.append([p,n])

for i in range(N+1):
    memo[i][0] = 1

for i in range(1,N+1):
    val, cnt = coins[i]
    for j in range(1,MONEY+1):
        memo[i][j] = memo[i-1][j]
    for c in range(1, cnt+1):
        for j in range(c*val, MONEY+1):
            memo[i][j] += memo[i-1][j - val * c]
print(memo[-1][-1])