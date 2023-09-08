import heapq

def solution(operations):
    minq = []
    maxq = []

    for oper in operations:
        oper = oper.split()
        op, num = oper[0], int(oper[1])
        if op == "I":
            heapq.heappush(minq, num)
            heapq.heappush(maxq, -num)
        else:
            if len(minq) != 0:
                if num == 1:
                    minq.remove(-heapq.heappop(maxq))
                else:
                    maxq.remove(-heapq.heappop(minq))

    if len(minq) == 0:
        return [0, 0]

    return [-heapq.heappop(maxq), heapq.heappop(minq)]