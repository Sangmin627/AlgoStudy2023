import sys

input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
x = int(input())
s.sort()
print(s)

j = n-1
i = 0
cnt = 0

while i < j:
    if s[i] + s[j] < x:
        i += 1
    elif s[i] + s[j] > x:
        j -= 1
    elif s[i] + s[j] == x:
        cnt += 1
        i += 1
        j -= 1

print(cnt)