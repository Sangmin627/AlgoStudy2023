n = int(input())

times = list(map(int, input().split()))
times.sort()

prefixSum = [0 for _ in range(n)]
prefixSum[0] = times[0]

for i in range(1, n):
    prefixSum[i] = prefixSum[i-1] + times[i]

print(sum(prefixSum))

