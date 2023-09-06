import copy

answer = []
max_diff = 1

def diff(lion, info):
    score_info = 0
    score_lion = 0
    for i in range(11):
        if lion[i] == info[i] == 0:
            continue

        if lion[i] > info[i]:
            score_lion += 10 - i
        else:
            score_info += 10 - i

    return score_lion - score_info


def dfs(n, lion, s, info):
    global answer
    global max_diff

    if n == 0:
        d = diff(lion, info)
        copy_lion = copy.deepcopy(lion)
        copy_lion.reverse()
        if d > max_diff:
            max_diff = d
            answer = [copy_lion]
        elif d == max_diff:
            answer.append(copy_lion)
        return

    for i in range(s, 11):
        lion[i] += 1
        n -= 1
        dfs(n, lion, i, info)
        lion[i] -= 1
        n += 1


def solution(n, info):
    lion = [0 for _ in range(11)]

    dfs(n, lion, 0, info)

    if not answer:
        return [-1]

    answer.sort(reverse=True)

    return list(reversed(answer[0]))