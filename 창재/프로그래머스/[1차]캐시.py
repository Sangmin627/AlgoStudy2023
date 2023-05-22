from collections import deque


def solution(cacheSize, cities):
    answer = 0

    q = deque(maxlen=cacheSize)
    for c in cities:
        lower_c = c.lower()

        if lower_c in q:
            answer += 1
            q.remove(lower_c) # 큐 에서 해당 요소 삭제
            q.append(lower_c)

        else:
            answer += 5
            q.append(lower_c)

    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))