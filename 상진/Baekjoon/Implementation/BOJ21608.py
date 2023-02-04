import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * n  for _  in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

scores = {1 : 0, 2 : 0, 3 : 0, 4 : 0}

resultBlank = [[0] * n for _ in range(n)]
resultLikes = [[0] * n for _  in range(n)]

answer = 0

def sitDown(nowStudent, resultLikes, resultBlank):
    result = []

    # 좋아하는 사람 주변에 없고, 빈 곳만 존재하는 경우
    if max(map(max, resultLikes)) == 0:
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    result.append((0, resultBlank[i][j], i, j))
        return result

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                result.append((resultLikes[i][j], resultBlank[i][j], i, j))
    return result

def calcualteScore(y, x, likes):
    adjCnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[ny][nx] in likes:
                adjCnt += 1
    if adjCnt != 0:
        scores[adjCnt] += 1

for i in range(n**2):
    nowStudent = students[i][0]
    likes = students[i][1:5]
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 0:
                blankCnt = 0
                likesCnt = 0
                for next in range(4):
                    nx = x + dx[next]
                    ny = y + dy[next]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[ny][nx] in likes:
                            likesCnt += 1
                        if not arr[ny][nx]:
                            blankCnt += 1
            resultBlank[y][x] = blankCnt
            resultLikes[y][x] = likesCnt
    result = sitDown(nowStudent, resultLikes, resultBlank)
    result.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))

    arr[result[0][2]][result[0][3]] = nowStudent

for i in range(n**2):
    nowStudent = students[i][0]
    likes = students[i][1:5]
    for y in range(n):
        for x in range(n):
            if arr[y][x] == nowStudent:
                calcualteScore(y, x, likes)

tmp = 0
for i in scores.values():
    answer += int(i * 10 ** tmp)
    tmp += 1

print(answer)