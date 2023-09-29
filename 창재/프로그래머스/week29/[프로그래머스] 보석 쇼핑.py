def solution(gems):
    answer = [0, 0]
    kinds = list(set(gems))

    # 딕셔너리 초기화
    kinds_dict = {}
    visited = {}
    visited_cnt = 0
    for k in kinds:
        kinds_dict[k] = 0
        visited[k] = False

    min_idx = 1
    max_idx = 1
    for i in range(len(gems)):
        kinds_dict[gems[i]] = i + 1
        max_idx = i + 1

        # 처음 한번만
        if not visited[gems[i]]:
            visited[gems[i]] = True
            visited_cnt += 1

            if visited_cnt == len(kinds):
                items = list(kinds_dict.values())
                items.sort()
                min_idx = items[0]
                answer = [min_idx, max_idx]

        # 그 뒤로는 이 조건에 따름.
        if visited_cnt >= len(kinds) and gems[i] == gems[min_idx - 1]:
            items = list(kinds_dict.values())
            items.sort()
            min_idx = items[0]

            if max_idx - min_idx < answer[1] - answer[0]:
                answer = [min_idx, max_idx]

    return answer