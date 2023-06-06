# 2X2 모양의 블럭 확인
def check(m, n, b):
    blocks = []
    for i in range(m - 1):
        for j in range(n - 1):
            if b[i][j] == 0:
                continue
            tmp = []
            tmp.append((i, j))
            now = b[i][j]
            if b[i + 1][j] == now:
                tmp.append((i + 1, j))

            if b[i][j + 1] == now:
                tmp.append((i, j + 1))

            if b[i + 1][j + 1] == now:
                tmp.append((i + 1, j + 1))

            if len(tmp) == 4:
                blocks.extend(tmp)
    return list(set(blocks))

def change(blocks, b):
    for y, x in blocks:
        b[y][x] = 0

def down(m, n, b):
    while True:
        flag = False
        for i in range(m - 1):
            for j in range(n):
                if b[i][j] and b[i + 1][j] == 0:
                    b[i + 1][j] = b[i][j]
                    b[i][j] = 0
                    flag = True
        if not flag:
            break

def solution(m, n, board):
    answer = 0
    b = []
    for line in board:
        b.append(list(line))

    while True:
        blocks = check(m, n, b)
        if not blocks:
            return answer
        answer += len(blocks)
        change(blocks, b)
        down(m, n, b)

    return answer