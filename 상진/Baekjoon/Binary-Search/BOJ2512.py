import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())

def binary(left, right):
    if left > right:
        print(right)
        return

    total = 0
    mid = (left + right) // 2
    for num in nums:
        if num <= mid:
            total += num
        else:
            total += mid
    if total <= M:
        binary(mid+1, right)
    else:
        binary(left, mid-1)

if sum(nums) <= M:
    print(nums[-1])
    exit()

binary(nums[0], nums[-1])

