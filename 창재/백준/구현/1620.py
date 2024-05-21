import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dogam = {}
for i in range(1, n + 1):
    pokectmon = input().rstrip()
    dogam[str(i)] = pokectmon
    dogam[pokectmon] = i

for _ in range(m):
    print(dogam[input().rstrip()])