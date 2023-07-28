import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    pq = list(map(int, input().split()))
    heapq.heapify(pq)
    ans = 0
    while len(pq) > 1:
        first = heapq.heappop(pq)
        second = heapq.heappop(pq)
        now = first + second
        ans += now
        heapq.heappush(pq, now)
    print(ans)