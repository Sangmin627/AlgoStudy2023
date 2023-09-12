import heapq

def solution(n, works):
    answer = 0
    q = [-i for i in works]
    heapq.heapify(q)

    while n > 0:
        num = heapq.heappop(q)
        if num < 0:
            heapq.heappush(q, num + 1)
            n -= 1
        else:
            return 0

    for i in q:
        answer += i ** 2
    return answer