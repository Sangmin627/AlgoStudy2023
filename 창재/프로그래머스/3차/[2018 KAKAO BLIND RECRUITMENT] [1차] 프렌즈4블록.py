def reBoard(m, n, board):
    return board


def remove_all(board, memo):
    sort_memo = list(memo)
    sort_memo.sort()
    for m in sort_memo:
        x, y = m[0], m[1]
        board[x][y] = '0'
        while x > 0 and board[x - 1][y] != '0':
            board[x][y] = board[x - 1][y]
            board[x - 1][y] = '0'

            x -= 1

    return board


def dfs(m, n, board):
    # 지울 칸 기록
    memo = set()
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    for x in range(m - 1):
        for y in range(n - 1):
            # 0 인 곳은 패스
            if board[x][y] == '0':
                continue

            unmatch_flag = False
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                if board[nx][ny] != board[x][y]:
                    unmatch_flag = True
                    break

            # 4칸이 안맞으면 아래는 패스!
            if unmatch_flag:
                continue

            memo.add((x, y))
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                memo.add((nx, ny))

    # memo 에 있던 좌표들 다 0으로 바꿔줌
    print(memo)
    if memo:
        board = remove_all(board, memo)
        return board, True
    else:
        return board, False


def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])

    flag = True
    while flag:
        # 같은게 있었는지 체크
        flag = False

        # 같은게 있는지 찾는 메소드
        board, flag = dfs(m, n, board)
        for i in range(m):
            print(board[i])
        print()

        # 비워진곳을 채우며 재배치
        board = reBoard(m, n, board)

    for i in range(m):
        answer += board[i].count('0')

    return answer

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
solution(m, n, board)