import sys

input = sys.stdin.readline
n = int(input())

dic = [0] * n
for i in range(n):
    dic[i] = input().rstrip()

print(dic)
a = sorted(set(dic))
print(a)
b = sorted(a, key=lambda x: len(x))
print(b)
print(*b)
print(*b, sep='\n')