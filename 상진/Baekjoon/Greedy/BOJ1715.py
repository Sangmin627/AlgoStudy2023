import sys, heapq
input = sys.stdin.readline

N = int(input())
pq = list(int(input()) for _ in range(N))
heapq.heapify(pq)

ans = 0
while len(pq) > 1:
    first = heapq.heappop(pq)
    second = heapq.heappop(pq)
    now = first + second
    ans += now
    heapq.heappush(pq, now)

print(ans)