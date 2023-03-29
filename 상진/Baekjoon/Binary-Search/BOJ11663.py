import sys
input = sys.stdin.readline

N,M = map(int, input().split())
points = sorted(list(map(int, input().split())))
lines = []

for i in range(M):
    s, e = map(int, input().split())
    l,r = 0, N-1
    end_idx, start_idx = -1,-1

    while l<=r:
        mid = (l+r) // 2
        if e < points[mid]:
            r = mid - 1
        else:
            l = mid + 1
    end_idx = r

    l = 0
    while l<=r:
        mid = (l+r) // 2
        if s <= points[mid]:
            r = mid - 1
        else:
            l = mid + 1
    start_idx = l

    if start_idx <= end_idx:
        print(end_idx-start_idx+1)
    else:
        print(0)