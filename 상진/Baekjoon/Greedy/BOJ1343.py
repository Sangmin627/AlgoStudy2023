board  = list(input())
board.append(".")

flag = True
countX = 0
answer = ""
for i in range(len(board)):
    if board[i] == "X":
        countX += 1
    else:
        if countX % 2 != 0:
            flag = False
            break
        else:
            if countX >= 4:
                answer += "A" * (countX // 4) * 4
                countX -= (countX // 4) * 4
            answer += "B" * (countX // 2) * 2
            countX -= (countX // 2) * 2
            answer += board[i]

if not flag:
    print(-1)
else:
    print(answer[:len(answer)-1])

