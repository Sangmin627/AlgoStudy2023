import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

memo = [0] * 367
for s,e in S:
    for i in range(s,e+1):
        memo[i] += 1

flag = False
start, end = 0, 0
width, max_height = 0, 0
ans = 0

for i in range(367):
    if memo[i] == 0:
        if flag:
            width = end - start
            ans += width * max_height
            flag = False
            max_height = 1
            start = i
        else:
            start = i
    else:
        max_height = max(max_height, memo[i])
        end = i
        flag = True

print(ans)