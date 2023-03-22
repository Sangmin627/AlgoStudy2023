import sys
input = sys.stdin.readline

N,X = map(int, input().split())
nums = list(map(int, input().split()))

val, max_val = 0, -1
e,s = 0,0
cnt = 1
for i in range(N):
    s = i
    while e-s != X and e < N:
        val += nums[e]
        e += 1

    if val > max_val:
        max_val = val
        cnt = 1
    elif val == max_val:
        cnt += 1

    if s == N-X:
        break
    else:
        val -= nums[s]

if max_val == 0:
    print("SAD")
else:
    print(max_val)
    print(cnt)