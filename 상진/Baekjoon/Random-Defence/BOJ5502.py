import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())
memo = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
   start = S[i-1]
   for j in range(1, N+1):
      rev = S[N-j]
      if start == rev:
         memo[i][j] = memo[i-1][j-1] + 1
      else:
         memo[i][j] = max(memo[i-1][j], memo[i][j-1])

print(N-memo[-1][-1])