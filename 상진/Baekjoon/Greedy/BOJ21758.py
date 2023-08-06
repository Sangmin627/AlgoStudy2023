import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

prefix_sum = [0] * N
suffix_sum = [0] * N
ans1, ans2, ans3 = 0,0,0

prefix_sum[0] = 0
for i in range(1,N):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

for i in range(1,N-1):
    ans1 = max(prefix_sum[-1] - prefix_sum[i] + prefix_sum[-1] - arr[i], ans1)

suffix_sum[-1] = 0
for i in range(N-2,-1,-1):
    suffix_sum[i] = suffix_sum[i+1] + arr[i]

for i in range(N-2,0,-1):
    ans2 = max(suffix_sum[0] - suffix_sum[i] + suffix_sum[0] - arr[i], ans2)

ans3 = sum(arr[1:N-1]) + max(arr[1:N-1])

print(max(ans1, ans2, ans3))