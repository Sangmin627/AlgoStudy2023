from collections import deque

# 오,아,왼,위
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def solution(board):
    n = len(board)
    MAX = int(1e9)
    answer = MAX
    costs = [[[MAX] * n for _ in range(n)] for _ in range(4)]  # costs[방향][y][x]
    q = deque()
    q.append((0, 0, 0, -1))  # y,x,cost,방향

    while q:
        y, x, c, dir = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            nc = c
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                if dir == -1:
                    nc += 100
                else:
                    if i != dir and abs(dir - i) != 2:
                        nc += 600
                    else:
                        nc += 100

                if nc < costs[i][ny][nx]:
                    costs[i][ny][nx] = nc
                    q.append((ny, nx, nc, i))

    for i in range(4):
        answer = min(answer, costs[i][-1][-1])

    return answer