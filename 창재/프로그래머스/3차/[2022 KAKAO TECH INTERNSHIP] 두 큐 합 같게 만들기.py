from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    sq1 = sum(q1)
    sq2 = sum(q2)

    total_count = len(q1) + len(q2)

    # 홀수면 노답.
    if (sq1 + sq2) % 2 == 1:
        return -1
    while sq1 != sq2:
        if answer > total_count:
            return -1

        while q2 and sq1 < sq2:
            x = q2.popleft()
            q1.append(x)
            sq1 += x
            sq2 -= x
            answer += 1

        while q1 and sq2 < sq1:
            x = q1.popleft()
            q2.append(x)
            sq2 += x
            sq1 -= x
            answer += 1

    return answer