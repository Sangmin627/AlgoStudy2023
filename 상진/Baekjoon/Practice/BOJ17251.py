import sys,heapq
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    arr[i] = -arr[i]

lq = []
cnt_r,cnt_b = 0,0
for i in range(1,N):
    left = arr[i-1]
    right = arr[i:]
    heapq.heappush(lq,left)
    heapq.heapify(right)
    if -lq[0] < -right[0]:
        cnt_b += 1
    elif -lq[0] > -right[0]:
        cnt_r += 1

# print(cnt_r, cnt_b)
if cnt_b > cnt_r:
    print("B")
elif cnt_b < cnt_r:
    print("R")
else:
    print("X")