import sys
import heapq

input = sys.stdin.readline
T = int(input())
for _ in range(T):

    N = int(input())
    heap = list(map(int, input().split()))

    heapq.heapify(heap)
    answer = 0
    while len(heap) > 1:
        file1 = heapq.heappop(heap)
        file2 = heapq.heappop(heap)
        sum_value = file1 + file2

        answer += sum_value

        heapq.heappush(heap, sum_value)

    print(answer)