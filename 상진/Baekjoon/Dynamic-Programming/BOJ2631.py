import sys
input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))
memo = [1] * N

for i in range(1,N):
    for j in range(i):
        if arr[j] < arr[i]:
            memo[i] = max(memo[i], memo[j] + 1)

print(N-max(memo))