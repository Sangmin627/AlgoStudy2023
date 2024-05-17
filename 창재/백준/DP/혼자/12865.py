import sys

# 향상된 DP
n, k = map(int, input().split())
k += 1

bag = {0: 0}
data = [tuple(map(int,input().split())) for _ in range(n)]
data.sort(reverse=True)

for w, v in data:

    tmp = {}
    for v_bag, w_bag in bag.items():
        if bag.get(nv := v + v_bag, k) > (nw := w + w_bag):
            tmp[nv]=nw

    bag.update(tmp)

print(max(bag.keys()))

# input = sys.stdin.readline
# n, k = map(int, input().split())
# dp = [0 for _ in range(k + 1)]
#
# for _ in range(n):
#     w, v = map(int, input().split())
#
#     if w > k:
#         continue
#
#     for i in range(k, w - 1, -1):
#         dp[i] = max(dp[i], dp[i - w] + v)
#
# print(dp[k])

# 5 7
# 10 13
# 7 7
# 4 8
# 3 6
# 5 12