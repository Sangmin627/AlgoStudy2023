import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(str, input().rstrip()))
INF = int(1e9)

memo = [INF] * N
BOJ = ["B","O","J"]
memo[0] = 0

for i in range(N):
    for k in range(3):
        if arr[i] == BOJ[k-1]:
            break
    for j in range(i+1, N):
        if arr[j] == BOJ[k]:
            memo[j] = min(memo[i] + (j-i)**2, memo[j])

if memo[-1] != INF:
    print(memo[-1])
else:
    print(-1)