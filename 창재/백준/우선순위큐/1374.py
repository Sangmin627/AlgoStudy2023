import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    num, start, end = map(int, input().split())

    heapq.heappush(heap, [start, end])

room = []

while heap:
    s, e = heapq.heappop(heap)

    if room:
        if s >= room[0]:
            heapq.heappop(room)

    heapq.heappush(room, e)

print(len(room))