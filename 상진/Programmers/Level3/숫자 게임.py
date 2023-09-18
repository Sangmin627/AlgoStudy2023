import heapq

def solution(A, B):
    answer = 0

    A = [-i for i in A]
    B.sort(reverse=True)

    heapq.heapify(A)
    idx = 0

    while A:
        now = -heapq.heappop(A)
        if now < B[idx]:
            answer += 1
            idx += 1

    return answer


