def printPan2D(Pan):
    for i in range(n):  # 세로 크기
        for j in range(n):  # 가로 크기
            print(Pan[i][j], end='')
        print()

if __name__ == '__main__':
    n = int(input())

    Pan = []
    for i in range(n):
        # Pan.append(list(input().replace('.', '0'))) # 이렇게 하고 싶었는데 replace는 문자열을 문자열로 바꿔줌.
        Pan.append(list(input()))  # 문자 하나씩 리스트 값으로 받아들임

    # 지뢰(*) 빼고 다 0으로 바꿈
    for x in range(n):
        for y in range(n):
            if Pan[x][y] == '.': Pan[x][y] = 0

    # 2차원 리스트 다 돌면서 * 일때, 그 주면 8개 칸에 +1
    for x in range(n):
        for y in range(n):
            if Pan[x][y] == '*':
                for sub_x in range(-1, 2): # 이렇게 해야 -1, 0, 1
                    for sub_y in range(-1, 2):
                        if 0 <= (x + sub_x) < n and 0 <= (y + sub_y) < n: # 없는칸이 아니면
                            if Pan[x + sub_x][y + sub_y] != '*':  # 들어 있는 값이 * 이면 안함.
                                Pan[x + sub_x][y + sub_y] += 1

    openPan = []
    for i in range(n):
        openPan.append(list(input()))

    gameOver_flag = False
    for i in range(n):
        for j in range(n):
            if openPan[i][j] == 'x':
                openPan[i][j] = Pan[i][j]
                if Pan[i][j] == '*':
                    gameOver_flag = True

    if gameOver_flag == True:
        for i in range(n):
            for j in range(n):
                if Pan[i][j] == '*':
                    openPan[i][j] = '*'

    printPan2D(openPan)


