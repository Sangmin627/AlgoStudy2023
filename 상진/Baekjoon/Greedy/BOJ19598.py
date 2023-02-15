import sys, heapq
input = sys.stdin.readline

n = int(input())
times = []
for _  in range(n):
    start, end = map(int, input().split())
    times.append((start, end))
times.sort(key=lambda x: x[0])

hq = [0]
for start, end in times:
    if start >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq, end)

print(len(hq))