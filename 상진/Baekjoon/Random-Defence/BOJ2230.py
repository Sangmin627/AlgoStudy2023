import sys, heapq
input = sys.stdin.readline

N,M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()

q= []

s, e = 0, 1
while s <= e and e < N:
    diff = nums[e] - nums[s]
    if diff > M:
        heapq.heappush(q, diff)
        s += 1
    elif diff == M:
        print(M)
        exit()
    else:
        e += 1

if len(q) == 0:
    print(0)
else:
    print(q[0])