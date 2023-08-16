import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

q = deque()
q.append(N)

visitied = [True for _ in range(100001)]

visitied[N] = 0

while q:
    x = q.popleft()
    if x == K:
        break
