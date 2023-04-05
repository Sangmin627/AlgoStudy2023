import sys


def back(start, a):
    memo.append(start)
    # print(memo)
    if len(memo) == k + 1:
        print(*memo, sep='')
        return 1

    if A[a] == "<":
        for i in range(start + 1, 10):
            if i not in memo:
                if back(i, a + 1) == 1:
                    return 1
                memo.pop()

    else:
        for i in range(start - 1, -1, -1):
            if i not in memo:
                if back(i, a + 1) == 1:
                    return 1
                memo.pop()

    return 0


input = sys.stdin.readline
k = int(input())
A = list(input().split())

memo = []   # 정답 기록을 위한 리스트
for s in range(10):
    if back(9 - s, 0) == 1:
        break
    memo.pop()

memo = []
for s in range(10):
    if back(s, 0) == 1:
        break
    memo.pop()