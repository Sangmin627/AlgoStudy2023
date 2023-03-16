import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
perm = list(permutations(map(str, range(1,N+1)), N))

for p in perm:
    print(" ".join(p))