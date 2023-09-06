def compress(s, i):
    temp = []
    x = 0
    y = x + i
    count = 1

    while 1:
        if y + i > len(s):
            if count > 1:
                temp.append(str(count))
            temp.append(s[x:x + i])
            temp.append(s[y:])
            break

        if s[x:x + i] == s[y:y + i]:
            count += 1
            y += i
        else:
            if count > 1:
                temp.append(str(count))
            temp.append(s[x:x + i])
            x = y
            y = x + i
            count = 1

    return ''.join(temp)


def solution(s):
    answer = 1000

    for i in range(1, len(s) // 2 + 1):
        c = compress(s, i)
        answer = min(answer, len(c))

    if len(s) == 1:
        answer = 1

    return answer