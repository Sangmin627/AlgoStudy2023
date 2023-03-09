import sys

input = sys.stdin.readline
n, m = map(int, input().split())
pre = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    pre[b].append(a)
print(pre)

memo = [0] * (n + 1)  # 0, 1, 0, 0, 1, 0, 1

# 여기서 괜히 시간 잡아 먹은듯, 그냥 마지막에 전체게 +1 해줘도 됐음.
for i in range(1, n + 1):
    if not pre[i]:
        memo[i] = 1

print(memo)

for i in range(1, n + 1):
    if memo[i] != 0:
        print(memo[i], end=' ')
        continue

    max_value = 0
    for p in pre[i]:
        max_value = max(max_value, memo[p] + 1)

    memo[i] = max_value

    print(memo[i], end=' ')