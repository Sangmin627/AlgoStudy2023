import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
a = ["a"] * operator[0]
b = ["b"] * operator[1]
c = ["c"] * operator[2]
d = ["d"] * operator[3]
abcd = a+b+c+d

permu = list(permutations(abcd, n - 1))
print(permu)
sol = []
for p in permu:
    answer = arr[0]
    for i in range(n - 1):
        if p[i] == "a":
            answer = answer + arr[i + 1]
        elif p[i] == "b":
            answer = answer - arr[i + 1]
        elif p[i] == "c":
            answer = answer * arr[i + 1]
        elif p[i] == "d":
            answer = answer // arr[i + 1]

    sol.append(answer)

sol.sort()
print(sol)
print(sol[-1])
print(sol[0])