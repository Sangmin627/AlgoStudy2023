def solution(n, t, m, p):
    answer = ''
    tmp = ' 0'
    idx = 0

    dic = dict()
    for i in range(10):
        dic[i] = str(i)

    for i in range(65, 71):
        dic[i - 55] = chr(i)

    for i in range(1, m * t + 1):
        num = i
        tmptmp = ''
        while num > 0:
            tmptmp += dic[num % n]
            num //= n
        tmp += tmptmp[::-1]

    while len(answer) != t:
        answer += tmp[p + m * idx]
        idx += 1

    return answer