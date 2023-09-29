def solution(gems):
    answer = []
    total_cnt = len(set(gems))
    dic = dict()
    dic[gems[0]] = 1
    start, end = 0, 0
    while start <= end and end < len(gems):
        if len(dic.keys()) == total_cnt:
            answer.append((start+1, end+1))
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] not in dic.keys():
                dic[gems[end]] = 1
            else:
                dic[gems[end]] += 1

    answer.sort(key=lambda x: (max(x) - min(x), min(x)))
    answer = [answer[0][0], answer[0][-1]]
    return answer