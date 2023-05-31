from collections import deque


def solution(queue1, queue2):
    answer = 0

    sq1 = deque(queue1)

    q1 = deque(queue1)
    q2 = deque(queue2)

    qsum1 = sum(q1)
    qsum2 = sum(q2)

    total = qsum1 + qsum2
    if total % 2 != 0:
        return -1

    target = total // 2
    if max(q1) > target or max(q2) > target:
        return -1

    while qsum1 != qsum2:
        if answer > 0 and q1 == sq1:
            return -1
        if qsum1 > qsum2:
            n = q1.popleft()
            q2.append(n)
            qsum1 -= n
            qsum2 += n
        elif qsum1 < qsum2:
            n = q2.popleft()
            q1.append(n)
            qsum2 -= n
            qsum1 += n
        answer += 1

    return answer