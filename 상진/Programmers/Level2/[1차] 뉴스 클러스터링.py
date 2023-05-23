def makeSub(str1, str2):
    sub1 = []
    sub2 = []

    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            sub1.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            sub2.append(str2[i:i + 2])

    return sub1, sub2

def cal(sub1, sub2):
    cnt = 0
    for i in sub1:
        if i in sub2:
            cnt += 1
            sub2.remove(i)

    if len(sub1) + len(sub2) == 0:
        return 65536
    else:
        return int((cnt / (len(sub1) + len(sub2))) * 65536)

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    sub1, sub2 = makeSub(str1, str2)
    answer = cal(sub1, sub2)

    return answer