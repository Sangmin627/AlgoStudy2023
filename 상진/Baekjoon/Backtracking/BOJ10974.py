import sys
input = sys.stdin.readline
N = int(input())
ans = []

def dfs():
    if len(ans) == N:
        print(*ans)
        return
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()
dfs()
