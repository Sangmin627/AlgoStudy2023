import sys
input = sys.stdin.readline

N,M = map(int, input().split())

names = []
uppers = []

for i in range(N):
    name, upper = map(str, input().split())
    names.append(name)
    uppers.append(int(upper))

def binary(left, right, power):
    if right < left:
        print(names[left])
        return
    mid = (left + right) // 2
    if power <= uppers[mid]:
        binary(left, mid-1, power)
    else:
        binary(mid+1, right, power)


for i in range(M):
    power = int(input())
    left, right = 0, N-1
    binary(left, right, power)