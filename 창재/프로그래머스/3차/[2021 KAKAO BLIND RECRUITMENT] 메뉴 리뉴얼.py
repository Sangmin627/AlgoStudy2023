from itertools import combinations

def solution(orders, course):
    answer = []
    l = len(orders)

    for c in course:
        comb = [[] for _ in range(l)]
        for i in range(l):
            comb[i] += list(combinations(sorted(list(orders[i])), c))

        all_comb = {}
        for i in range(l):
            for j in range(len(comb[i])):
                for m in range(i + 1, l):
                    if comb[i][j] in comb[m]:
                        if comb[i][j] not in all_comb:
                            all_comb[comb[i][j]] = 2
                        else:
                            all_comb[comb[i][j]] += 1
                        comb[m].remove(comb[i][j])

        if all_comb:
            max_value = max(all_comb.values())
            for k in all_comb:
                if all_comb[k] == max_value:
                    answer.append(''.join(k))
        print(answer)

    answer.sort()

    return answer