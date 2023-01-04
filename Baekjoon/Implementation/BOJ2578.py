board = []
answer = []
for i in range(5):
    board.append(list(map(int, input().split())))

for i in range(5):
    answer.append(list(map(int, input().split())))

def calBingo(board):
    bingo = 0
    # 가로
    for i in range(5):
        if sum(board[i]) == 0:
            bingo += 1

    # 세로
    for i in range(5):
        zeroCol = 0
        for j in range(5):
            if board[j][i] == 0:
                zeroCol += 1
            else:
                break
        if zeroCol == 5:
            bingo += 1

    # \
    rightToLeftDown = 0
    for i in range(5):
        if board[i][i] == 0:
            rightToLeftDown += 1
    if rightToLeftDown == 5:
        bingo += 1

    # /
    leftToRightUp = 0
    for i in range(5):
        if board[i][4-i] == 0:
            leftToRightUp += 1
    if leftToRightUp == 5:
        bingo += 1

    return bingo


cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        for n in range(5):
            for m in range(5):
                if answer[i][j] == board[n][m]:
                    board[n][m] = 0
        bingoCount = calBingo(board)
        if bingoCount >= 3:
            print(cnt)
            exit()
