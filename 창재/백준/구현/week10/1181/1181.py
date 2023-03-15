import sys

input = sys.stdin.readline
n = int(input())

dic = [0] * n
for i in range(n):
    dic[i] = input().rstrip()

a = list(set(dic))

b = sorted(a, key=lambda x: (len(x), x))

print(b)
print(*b)
print(*b, sep='\n')