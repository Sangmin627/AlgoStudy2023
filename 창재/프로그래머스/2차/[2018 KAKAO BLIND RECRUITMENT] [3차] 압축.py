def solution(msg):
    answer = []
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    dic = {}
    for i in range(26):
        dic[alphabet[i]] = i + 1

    len_msg = len(msg)
    i, j = 0, 1
    idx = 27
    while j <= len_msg:
        # j 가 i 보나 1 클때가 알파벳 하나.
        if msg[i:j] in dic.keys():
            j += 1
            continue
        else:
            answer.append(dic[msg[i:j - 1]])
            dic[msg[i:j]] = idx
            idx += 1
            i = j - 1
            j = i + 1

    answer.append(dic[msg[i:j - 1]])
    print(dic)
    print(answer)
    return answer

solution("KAKAO")