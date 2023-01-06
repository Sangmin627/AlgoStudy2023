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
        Pan.append(list(input()))  # 와 이게 되네!!! ㅆㅃ 이건 몰랐지

    for x in range(n):
        for y in range(n):
            if Pan[x][y] == '.': Pan[x][y] = 0

    for x in range(n):
        for y in range(n):
            if Pan[x][y] == '*':
                for sub_x in range(-1, 2): # 이렇게 해야 -1, 0, 1
                    for sub_y in range(-1, 2):
                        if 0 <= (x + sub_x) < n and 0 <= (y + sub_y) < n:
                            if Pan[x + sub_x][y + sub_y] != '*':
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


