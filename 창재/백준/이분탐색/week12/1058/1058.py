import sys

input = sys.stdin.readline
n = int(input())

network = [[] for _ in range(n + 1)]
memo = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    line = list(input())
    for j in range(n):
        if line[j] == 'Y':
            network[i].append(j + 1)

print(network)

for i in range(1, n + 1):
    for j in network[i]:
        for k in network[j]:
            if k != i and k not in network[i] and k not in memo[i]:
                memo[i].append(k)

for i in range(1, n + 1):
    network[i] += memo[i]
    print(network[i])
    network[i] = len(network[i])

print(network)
print(max(network[1:]))