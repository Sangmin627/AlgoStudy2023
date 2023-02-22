from collections import deque
import sys
input = sys.stdin.readline

max_size = 100001
N, K = map(int, input().split())
times = [-1] * max_size

g = [[] * max_size for _ in range(max_size)]

g[0].append((0,0,1))
for i in range(1, max_size):
    g[i].append((2*i, i-1, i+1))

q = deque()
q.append(N)
times[N] = 0
while q:
    now = q.popleft()
    if now == K:
        print(times[K])
        break
    for nexts in g[now]:
        for i in range(3):
            if nexts[i] < max_size and times[nexts[i]] == -1:
                q.append(nexts[i])
                if i == 0:
                    times[nexts[i]] = times[now]
                else:
                    times[nexts[i]] = times[now] + 1
