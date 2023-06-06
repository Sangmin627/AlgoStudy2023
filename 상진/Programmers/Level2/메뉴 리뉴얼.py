from itertools import combinations

def solution(orders, course):
    answer = []
    odict = dict()

    for order in orders:
        for i in range(2, len(order) + 1):
            comb = list(combinations(sorted(order), i))
            for c in comb:
                cs = "".join(c)
                if cs not in odict.keys():
                    odict[cs] = 1
                else:
                    odict[cs] += 1

    for c in course:
        tmps = []
        for key in odict.keys():
            if len(key) == c and odict[key] >= 2:
                tmps.append([odict[key], key])

        tmps.sort(reverse=True)
        if not tmps:
            continue

        max_count = tmps[0][0]
        for tmp in tmps:
            if tmp[0] < max_count:
                break
            answer.append(tmp[1])

    answer.sort()
    return answer
