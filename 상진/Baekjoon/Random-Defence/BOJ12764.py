import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x : (x[0], (x[1]-x[0])))

seats = [0] * N

places = [i for i in range(N)]
heapq.heapify(places)
q = []

for i in range(N):
    start = arr[i][0]
    end = arr[i][1]
    if not q or start < q[0][0]:
        idx = heapq.heappop(places)
        seats[idx] += 1
        heapq.heappush(q, (end, idx))
    else:
        while q:
            if start < q[0][0]:
                break
            before_end, before_idx = heapq.heappop(q)
            heapq.heappush(places, before_idx)

        idx = heapq.heappop(places)
        seats[idx] += 1
        heapq.heappush(q, (arr[i][1], idx))

ans = []
cnt = 0
for i in seats:
    if i != 0:
       cnt += 1
       ans.append(i)

print(cnt)
print(*ans)