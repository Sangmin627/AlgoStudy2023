def searchIndex(str):
    for i in range(3):
        for j in range(10):
            if keyboard[i][j] == str:
                return [i, j]

def distance(last, cur):
    dis = abs((last[0] - cur[0])) + abs((last[1] - cur[1]))
    return dis


if __name__ == '__main__':
    keyboard = []
    keyboard.append(list("qwertyuiop"))
    keyboard.append(list("asdfghjkl "))
    keyboard.append(list("zxcvbnm   "))

    a = list(input().replace(' ', ''))
    start_L = searchIndex(a[0]) # 왼손 시작점
    start_R = searchIndex(a[1]) # 오른손 시작점

    b = list(input())
    ZOAC = []
    for i in b:
        ZOAC.append(searchIndex(i))

    sum = 0
    last_L, last_R = start_L, start_R
    for s in ZOAC:
        if s[0] <= 1:
            if s[1] <= 4:
                sum += distance(last_L, s) + 1
                last_L = s
            else:
                sum += distance(last_R, s) + 1
                last_R = s
        else:
            if s[1] <= 3:
                sum += distance(last_L, s) + 1
                last_L = s
            else:
                sum += distance(last_R, s) + 1
                last_R = s

    print(sum)