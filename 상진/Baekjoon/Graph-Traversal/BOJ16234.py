from collections import deque
import sys
input = sys.stdin.readline

dy = [-1,0,1,0]
dx = [0,-1,0,1]

N,L,R = map(int, input().split())
g = []
for i in range(N):
    g.append(list(map(int, input().split())))

answer = 0
flag = False

def check():
    total_union_q = deque()
    global flag, visited
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                each_union_q = bfs(i,j)
                if len(each_union_q) <= 1:
                    continue
                flag = True
                total_union_q.append(each_union_q)
    return total_union_q

def bfs(y,x):
    global visited
    q = deque()
    each_union_q = deque()
    visited[y][x] = 1
    q.append((y,x))
    each_union_q.append((y,x))
    while q:
        y,x = q.popleft()
        now = g[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                next = g[ny][nx]
                if not visited[ny][nx] and L <= abs(next - now) <= R:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    each_union_q.append((ny, nx))
    return each_union_q

def cal(total_union_q):
    while total_union_q:
        each_union_q = total_union_q.popleft()
        union_cnt = len(each_union_q)
        union_val = 0
        for y,x in each_union_q:
            union_val += g[y][x]
        while each_union_q:
            y,x = each_union_q.popleft()
            g[y][x] = union_val // union_cnt

while True:
    flag = False
    visited = [[0] * N for _ in range(N)]
    total_union_q = check()
    if flag:
        answer += 1
        cal(total_union_q)
        continue
    else:
        print(answer)
        break
