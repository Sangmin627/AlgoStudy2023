import sys

input = sys.stdin.readline
N = int(input())
calender = [0 for _ in range(366)]

for i in range(N):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        calender[i] += 1

answer = 0
start_idx = 1
max_high = 0
i = 1
while i < 366:
    if calender[i] == 0:
        answer += (i - start_idx) * max_high
        # print("i = ", i,", answer = ", answer)
        start_idx = i + 1
        max_high = 0
    else:
        max_high = max(max_high, calender[i])

    i += 1

answer += (i - start_idx) * max_high
print(answer)