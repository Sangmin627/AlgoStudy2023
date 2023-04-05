from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
X,Y = map(int, input().split())

dy = [1,1,-1,-1,2,2,-2,-2]
dx = [-2,2,-2,2,-1,1,-1,1]

enemy_pos = []
ans = []

for _ in range(M):
    enemy_pos.append(list(map(int, input().split())))

visited = [[-1] * N for _ in range(N)]
visited[Y-1][X-1] = 0
q = deque()
q.append([Y-1, X-1])
while q:
    y, x = q.popleft()
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])

for y,x in enemy_pos:
    ans.append(visited[x-1][y-1])
print(*ans)




