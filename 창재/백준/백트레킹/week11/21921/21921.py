import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))

window = sum(visit[:x])
answer = [window]

for i in range(x, n):
    window += visit[i] - visit[i - x]
    answer.append(window)

max_v = max(answer)
cnt = answer.count(max_v)

if max_v == 0:
    print("SAD")
else:
    print(max_v)
    print(cnt)
