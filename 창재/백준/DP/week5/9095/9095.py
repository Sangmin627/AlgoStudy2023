import sys

input = sys.stdin.readline
T = int(input())


def sol(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return sol(N - 1) + sol(N - 2) + sol(N - 3)


for i in range(T):
    N = int(input())
    print(sol(N))

