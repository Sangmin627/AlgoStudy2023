import sys
input = sys.stdin.readline

N,M,H = map(int, input().split())
arr = [sorted(list(map(int, input().split()))) for _ in range(N)]
memo = [[0] * (H+1) for _ in range(N+1)]

for i in range(N+1):
    memo[i][0] = 1

for i in range(1,N+1):
    for j in range(1,H+1):
        memo[i][j] = memo[i-1][j]
        for k in arr[i-1]:
            if j >= k:
                memo[i][j] += memo[i-1][j-k]

print(memo[-1][-1] % 10007)
