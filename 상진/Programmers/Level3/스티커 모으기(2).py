import copy

def solution(sticker):
    answer = 0
    size = len(sticker)
    if size <= 3:
        if size == 3:
            return max(sticker[0] + sticker[2], sticker[1])
        return max(sticker)

    sticker1 = copy.deepcopy(sticker)
    sticker1.pop()
    sticker2 = copy.deepcopy(sticker)
    sticker2.pop(0)

    memo1 = [0] * size
    memo2 = [0] * size

    memo1[0], memo1[1] = sticker1[0], max(sticker1[0], sticker1[1])
    memo2[0], memo2[1] = sticker2[0], max(sticker2[0], sticker2[1])

    for i in range(2, size - 1):
        memo1[i] = max(memo1[i - 1], memo1[i - 2] + sticker1[i])
        memo2[i] = max(memo2[i - 1], memo2[i - 2] + sticker2[i])
        answer = max(memo1[i], memo2[i])

    return answer