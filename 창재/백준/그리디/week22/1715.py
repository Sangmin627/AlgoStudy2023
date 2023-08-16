import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    heapq.heappush(heap, int(input()))

# print(heap)

if N == 1:
    print(0)
elif N == 2:
    print(sum(heap))
else:
    answer = 0
    while len(heap) > 1:
        card1 = heapq.heappop(heap)
        card2 = heapq.heappop(heap)
        sum_value = card1 + card2

        answer += sum_value

        heapq.heappush(heap, sum_value)
        # print(heap)

    print(answer)