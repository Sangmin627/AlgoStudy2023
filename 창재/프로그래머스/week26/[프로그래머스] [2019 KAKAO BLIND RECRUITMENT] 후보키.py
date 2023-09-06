from itertools import combinations as comb

def isMinimality(c, candidate_key):
    set_c = set(c)
    for k in candidate_key:
        set_k = set(k)
        if set_k.issubset(set_c):
            return False

    return True

def solution(relation):
    answer = 0

    l_col = len(relation[0])  # 속성 개수
    l_row = len(relation)  # 값 개수

    col = [i for i in range(l_col)]

    candidate_key = []

    for i in range(1, l_col + 1):
        for c in list(comb(col, i)):
            if not isMinimality(c, candidate_key):
                continue

            temp = [tuple(relation[x][y] for y in c) for x in range(l_row)]
            print(temp)
            if len(temp) == len(set(temp)):
                candidate_key.append(c)

        print(candidate_key)

    answer = len(candidate_key)
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))