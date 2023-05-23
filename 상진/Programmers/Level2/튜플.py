def solution(s):
    answer = []
    s = s[2:-2]
    arr = s.split("},{")
    arr.sort(key=lambda x: len(x))
    for i in arr:
        tmp = i.split(",")
        for j in tmp:
            if int(j) not in answer:
                answer.append(int(j))

    return answer