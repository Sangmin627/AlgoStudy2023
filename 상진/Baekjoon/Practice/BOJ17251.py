import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

cnt_r, cnt_b = 0,0
max_val = max(arr)
index_list = []

for i in range(N):
    if max_val == arr[i]:
        index_list.append(i)

if len(index_list) == 1:
    idx = index_list[0]
    cnt_b = idx
    cnt_r = N - 1 - idx
else:
    min_idx,max_idx = index_list[0],index_list[-1]
    cnt_b = min_idx
    cnt_r = N - 1 - max_idx

if cnt_b < cnt_r :
    print("R")
elif cnt_b > cnt_r:
    print("B")
else:
    print("X")