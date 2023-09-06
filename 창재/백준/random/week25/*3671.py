import sys
from itertools import permutations

# 에라토스테네스의 체
n=10000000
primes = [False,False] + [True]*(n-1)

for i in range(2,int(n ** 0.5) + 1):
  if primes[i]:
    for j in range(2*i, n+1, i):
        primes[j] = False


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = list(input().rstrip())

    count = 0
    memo = set()
    for i in range(1, len(N) + 1):
        C = list(permutations(N, i))
        for c in C:
            a = int(''.join(c))
            memo.add(a)

    for s in list(memo):
        if primes[s]:
            count += 1

    print(count)