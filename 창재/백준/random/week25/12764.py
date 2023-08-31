import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = []
for i in range(N):
    s, e = map(int, input().split())
    heapq.heappush(heap, (s, e))

record = [0 for _ in range(N)]
answer = [0 for _ in range(N)]
count = 0

while heap:
    h = heapq.heappop(heap)
    s, e = h[0], h[1]

    for i in range(N):
        if record[i] <= s:
            if record[i] == 0:
                count += 1
            record[i] = e
            answer[i] += 1
            break

print(count)
for a in answer:
    if a == 0:
        break
    print(a, end=' ')