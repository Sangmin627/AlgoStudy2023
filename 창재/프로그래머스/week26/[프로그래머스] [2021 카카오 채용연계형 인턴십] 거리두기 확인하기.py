dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(place, x, y, visited):
    if visited[x][y] >= 2:
        return False

    if place[x][y] == "X":
        return False

    for n in range(4):
        nx = x + dx[n]
        ny = y + dy[n]
        if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == -1:
            if place[nx][ny] == "P":
                return True
            else:
                visited[nx][ny] = visited[x][y] + 1
                if dfs(place, nx, ny, visited):
                    return True

    return False

def solution(places):
    answer = []

    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    visited = [[-1 for _ in range(5)] for _ in range(5)]
                    visited[i][j] = 0
                    if dfs(place, i, j, visited):
                        flag = 0
                        break

            if flag == 0:
                break

        answer.append(flag)

    return answer