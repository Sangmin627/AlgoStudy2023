from collections import deque

def solution(stones, k):
    answer = 200000001
    q = deque()

    for i in range(len(stones)):
        while q and q[0][1] < i - k + 1:
            q.popleft()
        while q and q[-1][0] < stones[i]:
            q.pop()
        q.append((stones[i], i))
        if i >= k - 1:
            answer = min(answer, q[0][0])

    return answer