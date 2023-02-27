import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    memo = [0] * (money+1)
    memo[0] = 1
    for i in range(1, N+1):
        for j in range(coins[i], money+1):
            memo[j] += memo[j-coins[i]]
    print(memo[-1])
