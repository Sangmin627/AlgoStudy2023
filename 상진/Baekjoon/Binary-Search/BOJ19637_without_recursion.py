import sys
input = sys.stdin.readline

N,M = map(int, input().split())

names = []
uppers = []

for i in range(N):
    name, upper = map(str, input().split())
    names.append(name)
    uppers.append(int(upper))

for i in range(M):
    left, right = 0, N - 1
    power = int(input())
    while left <= right:
        mid = (left + right) // 2
        if power <= uppers[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print(names[left])