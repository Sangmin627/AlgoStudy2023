import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x >= N or y >= N:
        return 0

    if dp[x][y] != -1:
        return dp[x][y]

    if left[x] > right[y]:
        dp[x][y] = dfs(x, y + 1) + right[y]
        return dp[x][y]
    else:
        dp[x][y] = max(dfs(x + 1, y), dfs(x + 1, y + 1))
        return dp[x][y]


input = sys.stdin.readline
N = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
dp = [[-1 for _ in range(N)] for _ in range(N)]

dfs(0, 0)
print(dp[0][0])

for d in dp:
    print(*d)
print()