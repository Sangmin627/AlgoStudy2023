def solution(msg):
    answer = []
    dic = {}
    dic_idx = 1
    for i in range(65, 91):
        dic[chr(i)] = dic_idx
        dic_idx += 1

    s, e = 0, 1
    while e < len(msg):
        n = msg[s:e + 1]
        if n not in dic.keys():
            dic[n] = dic_idx
            dic_idx += 1
            answer.append(dic[msg[s:e]])
            s = e
            e += 1
        else:
            e += 1

    answer.append(dic[msg[s:e]])
    return answer