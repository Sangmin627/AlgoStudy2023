import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = [0] * n
for i in range(n):
    arr[i] = int(input())

arr.sort()
print(arr)

i = 0
j = 0
min_value = int(1e10)   # 개 빡치누
print(min_value)
while i <= j < n:
    a = arr[j] - arr[i]

    if a == m:
        min_value = a
        break

    elif a < m:
        j += 1
        continue

    else:
        min_value = min(min_value, a)
        i += 1


print(arr[i])
if min_value == int(1e10):
    print(0)
else:
    print(min_value)