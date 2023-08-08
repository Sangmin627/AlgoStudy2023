import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    memo = [[0] * (M+1) for _ in range(N+1)]

    for i in range(1,M+1):
        memo[1][i] = i

    for i in range(2,N+1):
        for j in range(2**(i-1), M+1):
            memo[i][j] = memo[i][j-1] + memo[i-1][j//2]
    print(memo[-1][-1])