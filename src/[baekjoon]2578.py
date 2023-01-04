def hor_sum(bingo_pan, x):
    hor_sum = 0
    for i in range(5):
        hor_sum += bingo_pan[x][i]

    if hor_sum == 0 : return 1
    else: return 0


def ver_sum(bingo_pan, y):
    ver_sum = 0
    for i in range(5):
        ver_sum += bingo_pan[i][y]

    if ver_sum == 0 : return 1
    else: return 0


def cross1_sum(bingo_pan):
    cross1_sum = 0
    for i in range(5):
        cross1_sum += bingo_pan[i][i]

    if cross1_sum == 0: return 1
    else: return 0


def cross2_sum(bingo_pan):
    cross2_sum = 0
    for i in range(5):
        cross2_sum += bingo_pan[4-i][i]

    if cross2_sum == 0: return 1
    else: return 0


def matching(bingo_pan, correct):
    number, x, y = 0, 0, 0
    bingo_count = 0
    bingo_flag = False

    for number, value in enumerate(correct):
        matching_flag = False
        for x in range(5):
            for y in range(5):
                if bingo_pan[x][y] == value :
                    bingo_pan[x][y] = 0
                    if x == y: bingo_count += cross1_sum(bingo_pan)  # 좌상향 대각선
                    if x+y == 4: bingo_count += cross2_sum(bingo_pan)  # 우상향 대각선
                    bingo_count += hor_sum(bingo_pan, x) + ver_sum(bingo_pan, y)

                    if bingo_count >= 3:
                        bingo_flag = True
                        break

                    matching_flag = True
                    break

            if matching_flag == True or bingo_flag == True:
                break

        if bingo_flag == True: break

    return number


if __name__ == '__main__':
    bingo_pan = []
    for i in range(5):
        bingo_pan.append(list(map(int, input().split())))

    correct = []
    for i in range(5):
        correct_line = list(map(int, input().split()))
        for j in range(5):
            correct.append(correct_line[j])

    final = matching(bingo_pan, correct) + 1  # 결과는 index임으로 +1 해줘야함
    print(final)