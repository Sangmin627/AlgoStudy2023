import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

max_value = max(arr)
h = []

for i in range(n):
    if arr[i] == max_value:
        h.append(i)

s, e = h[0], h[-1]

if s == (n - 1) - e:
    print("X")
elif s < (n - 1) - e:
    print("R")
else:
    print("B")