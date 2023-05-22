import sys
input = sys.stdin.readline

A,B = map(int, input().split())

ans = 0
for i in range(1,11):
    ans += 2 ** i

nums = [0] * 2046
nums[0],nums[1] = 4, 7
nums[2],nums[3],nums[4], nums[5] = 44, 47, 74, 77

idx = 3
for i in range(6, len(nums)):
    if nums[i] != 0:
        continue
    tmp_idx = 0
    for j in range(i, i+2**idx-1, 2):
        nums[j] = int(str(nums[j - 2**(idx-1)-tmp_idx]) + str(nums[0]))
        nums[j+1] = int(str(nums[j - 2**(idx-1)-tmp_idx]) + str(nums[1]))
        tmp_idx += 1
    idx += 1

s_idx, e_idx = 0,0
for i in range(len(nums)):
    if A > nums[i]:
        s_idx = i+1
    if nums[i] > B:
        e_idx = i
        break

print(e_idx - s_idx)
