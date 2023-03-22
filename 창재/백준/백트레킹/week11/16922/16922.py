import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
n = int(input())

loma = [1, 5, 10, 50]
com = list(combinations_with_replacement(loma, n))
print(com)
print(len(com))

for i in range(len(com)):
    com[i] = sum(com[i])

print(com)
print(sorted(com))

print(len(set(com)))