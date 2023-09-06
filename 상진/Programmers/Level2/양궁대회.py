import copy

def calculate_score_diff(apeach, ryan):
    apeach_score = 0
    ryan_score = 0
    for i in range(11):
        if apeach[i] >= ryan[i]:
            if apeach[i] != 0:
                apeach_score += 10 - i
        else:
            ryan_score += 10 - i
    return ryan_score - apeach_score

def back(idx, depth, n, ryan, apeach, dic):
    if depth == n:
        score_diff = calculate_score_diff(apeach, ryan)
        if score_diff > 0:
            if score_diff not in dic.keys():
                dic[score_diff] = [copy.deepcopy(ryan)]
            else:
                dic[score_diff].append(copy.deepcopy(ryan))
        return

    for i in range(idx,11):
        if ryan[i] > apeach[i]:
            continue
        if calculate_score_diff(apeach, ryan) > 0:
            ryan[i] += 1
            back(i, depth+1, n, ryan, apeach, dic)
            ryan[i] -= 1
        else:
            diff = apeach[i] + 1
            if depth + diff <= n:
                ryan[i] += diff
                back(i+1, depth + diff, n, ryan, apeach, dic)
                ryan[i] -= diff

def solve_answer(dic):
    keys = sorted(dic.keys(), reverse=True)
    if len(keys) == 0:
        return [-1]

    key = keys[0]
    if len(dic[key]) == 1:
        return dic[key][0]
    else:
        ans = dic[key][0]
        for i in range(10,-1,-1):
            for val in dic[key]:
                if val[i] != 0 and ans[i] < val[i]:
                    ans = val
            if ans[i] != 0:
                break
        return ans

def solution(n, apeach):
    dic = dict()
    ryan = [0] * 11
    back(0, 0, n, ryan, apeach, dic)
    answer = solve_answer(dic)
    return answer