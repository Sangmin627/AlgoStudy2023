import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))
X = int(input())

s,e = 0,N-1
ans = 0

while s < e:
    if nums[s] + nums[e] > X:
        e -= 1
        continue
    if nums[s] + nums[e] == X:
        ans += 1
    s += 1

print(ans)