import sys
from itertools import product

input = sys.stdin.readline
A, B = map(int, input().split())

a = list(str(A))
b = list(str(B))

print(a)
print(b)

answer = 0
for i in range(len(a), len(b) + 1):  # i는 자리 수이기 때문에 b의 자리수까지 계산 해야댐
    for p in product([4, 7], repeat=i):
        p = int(''.join(map(str, p)))
        print(p)
        if A <= p <= B:
            answer += 1
        elif B < p:
            break

print(answer)


