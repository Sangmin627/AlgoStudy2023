import sys
input = sys.stdin.readline

N,M = map(int, input().split())
ans = 0
visited = [[0] * (M+1) for _ in range(N+1)]

def is_squared(y,x):
    if visited[y][x-1] == visited[y-1][x] == visited[y-1][x-1] == 1:
        return True
    return False

def back(y,x):
    global ans
    if y == N and x == M-1:
        ans += 1
        return

    if y == N:
        x += 1
        y = 0

    back(y+1, x)

    if not is_squared(y,x):
        visited[y][x] = 1
        back(y+1, x)
        visited[y][x] = 0

back(0,0)
print(ans)
