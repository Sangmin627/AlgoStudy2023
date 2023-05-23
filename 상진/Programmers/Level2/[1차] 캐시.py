from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()

    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            if len(q) == cacheSize:
                q.popleft()
            q.append(city)
            answer += 5

    return answer