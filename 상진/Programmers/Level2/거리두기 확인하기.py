from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(sy, sx, place):
    q = deque()
    visited = [[-1] * 5 for _ in range(5)]
    q.append((sy, sx))
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if visited[ny][nx] == -1 and place[ny][nx] != 'X':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
                    if place[ny][nx] == 'P' and visited[ny][nx] <= 2:
                        return False
    return True

def solution(places):
    answer = []
    for place in places:
        people = []
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))

        for y, x in people:
            if not bfs(y, x, place):
                flag = False
                break

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer