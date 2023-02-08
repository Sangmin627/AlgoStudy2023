from itertools import combinations

n = input()

odds = ["1","3","5","7","9"]
combiNumbers = "123456789"

minAnswer = int(1e9)
maxAnswer = -1

def countOdd(num):
    cnt = 0
    for i in num:
        if i in odds:
            cnt += 1
    return cnt

def slice(num, ans):
    global minAnswer, maxAnswer, combiNumbers
    ans += countOdd(num)
    size = len(num)
    if size >= 3:
        afterCombiNumber = combiNumbers[:size-1]
        combi = list(combinations(afterCombiNumber, 2))
        for s, e in combi:
            start = num[0:int(s)]
            middle = num[int(s):int(e)]
            end = num[int(e):]
            calNum = str(int(start) + int(middle) + int(end))
            slice(calNum, ans)
    elif size == 2:
        calNum = str(int(num[0]) + int(num[1]))
        slice(calNum, ans)
    else:
        minAnswer = min(minAnswer, ans)
        maxAnswer = max(maxAnswer, ans)
        return

slice(n, 0)
print(minAnswer, maxAnswer)