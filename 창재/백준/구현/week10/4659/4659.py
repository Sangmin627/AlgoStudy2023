import sys

input = sys.stdin.readline

while True:
    prob = list(input().rstrip())
    if prob == list('end'):
        exit()

    mo = list('aeiou')

    i = 0

    cnt_mo = 0  # 모음 연속 count
    cnt_ja = 0  # 자음 연속 count

    flag = False    # 모음 한개 라도 있으면 True

    while i < len(prob):
        if prob[i] in mo:   # 모음 이면
            flag = True
            cnt_mo += 1
            cnt_ja *= 0
        else:
            cnt_mo *= 0
            cnt_ja += 1

        if cnt_mo == 3 or cnt_ja == 3:  # 자음이든 모음이든 3번 연속으로 나오면 탈출
            flag = False
            break

        if i < len(prob) - 1 and prob[i] == prob[i + 1]:    # 연속으로 같은 글자가 나오면 탈출
            if prob[i] == 'e' or prob[i] == 'o':    # 얘넨 예외
                i += 1
                continue
            else:
                flag = False
                break

        i += 1

    if flag:
        print('<' + ''.join(prob) + '> is acceptable.')
    else:
        print('<' + ''.join(prob) + '> is not acceptable.')