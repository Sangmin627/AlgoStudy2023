import sys
input = sys.stdin.readline

g = list(list(input().split()) for _ in range(5))
ans = set()

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(sy,sx,tmp):
    tmp += g[sy][sx]
    if len(tmp) == 6:
        ans.add(tmp)
        return
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
            dfs(ny,nx,tmp)

for i in range(5):
    for j in range(5):
        tmp = ""
        dfs(i,j,tmp)

print(len(ans))