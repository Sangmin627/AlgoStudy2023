import sys
input = sys.stdin.readline

D,P = map(int, input().split())
arr = sorted(list(map(int, input().split())) for _ in range(P))
memo = [0] * (D+1)
memo[arr[0][0]] = arr[0][1]

for i in range(1,P):
    l,w = arr[i][0], arr[i][1]
    for j in range(l,D+1):
        if memo[j-l] != 0:
            memo[j] = max(memo[j], min(memo[j-l], w))
    memo[l] = max(memo[l], w)

print(memo[-1])

