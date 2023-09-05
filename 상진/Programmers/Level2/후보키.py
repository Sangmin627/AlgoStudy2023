from itertools import combinations

def is_minimality(key_idx, candidates):
    for candidate in candidates:
        cnt = 0
        size = len(candidate)
        for c in candidate:
            if c in key_idx:
                cnt += 1
        if cnt == size:
            return False
    return True

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    re = [i for i in range(col)]
    candidates = []

    for c in range(col):
        combs = list(combinations(re, c + 1))
        for comb in combs:
            s = set()
            key_idx = "".join(map(str, comb))

            if is_minimality(key_idx, candidates):
                for r in range(row):
                    tmp = ""
                    for i in comb:
                        tmp += relation[r][i]
                    s.add(tmp)
                if len(s) == row:
                    candidates.append(key_idx)
    return len(candidates)
