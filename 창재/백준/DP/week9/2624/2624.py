import sys

input = sys.stdin.readline

t = int(input())
k = int(input())
coin = [[int(x) for x in input().split()] for _ in range(k)]

coin.sort()

dp = [0] * (t + 1)
dp[0] = 1

print(coin)
print(dp)

for c in coin:
    for j in range(c[0], t + 1):

        dp[j] += dp[j - c[0]]
        if j % c[0] == 0:
            if c[1] == 0:
                dp[j] -= 1
                break
            c[1] -= 1

    print(c, ' : ', dp)

print(dp)

# for i in range(t + 1):
#     if dp[i] == 0:
#         dp[i] = -1

print(dp)
print(dp[t])