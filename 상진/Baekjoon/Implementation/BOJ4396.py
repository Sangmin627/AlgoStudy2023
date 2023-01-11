n = int(input())

board = []
myInput = []
answer = [["."] * n for _ in range(n)]
bomb = []

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

flag = True
for x in range(n):
    board.append(list(input()))
    for y in range(n):
        if board[x][y] == "*":
            bomb.append((x, y))

for x in range(n):
    myInput.append(list(input()))
    for y in range(n):
        if myInput[x][y] == "x" and (x,y) in bomb:
            flag = False

def calculateNumber():
    for x in range(n):
        for y in range(n):
            if myInput[x][y] == "x":
                cnt = 0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if (nx, ny) in bomb:
                            cnt += 1
                answer[x][y] = cnt

if not flag:
    calculateNumber()
    for x in range(n):
        for y in range(n):
            if (x,y) in bomb:
                answer[x][y] = "*"

    for x in range(n):
        for y in range(n):
            print(answer[x][y], end="")
        print()

else:
    calculateNumber()
    for x in range(n):
        for y in range(n):
            print(answer[x][y], end="")
        print()


