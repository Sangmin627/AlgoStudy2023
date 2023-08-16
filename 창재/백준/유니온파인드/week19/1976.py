import sys
# limit_number = 500000 # n <= 500,000 이므로
# sys.setrecursionlimit(limit_number)

def find(a):
    if a == memo[a]:
        return a
    else:
        memo[a] = find(memo[a])

    return memo[a]

input = sys.stdin.readline
n = int(input()) # <= 200
m = int(input()) # <= 1000

memo = [i for i in range(n + 1)]

for i in range(n):
    line = list(map(int, input().split()))

    for j in range(i + 1, n):
        if line[j]:
            fi = find(i + 1)
            fj = find(j + 1)
            super = min(fi, fj)
            memo[fi] = super
            memo[fj] = super

path = list(map(int, input().split()))
fp = find(path[0])

for p in path:
    if fp != find(p):
        print("NO")
        sys.exit()

print("YES")
