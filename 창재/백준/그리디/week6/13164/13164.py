import sys

input = sys.stdin.readline
N, K = map(int, input().split())
child = list(map(int, input().split()))

# append 보다 이게 좀더 빠름.
dif = [0] * (N-1)
for i in range(N-1):
    dif[i] = child[i+1] - child[i]

print('dif : ', dif)
dif.sort(reverse=True)
print('dif : ', dif)

print(sum(dif[K-1:]))

# 9 4
# 1 3 5 6 10 11 15 18 20