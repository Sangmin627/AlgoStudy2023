import sys
input = sys.stdin.readline

memo = [0] * 12
memo[1], memo[2], memo[3] = 1, 2, 4

for i in range(4, 12):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

T = int(input())
answer = [0] * T

for i in range(T):
    n = int(input())
    answer[i] = memo[n]

for i in answer:
    print(i)