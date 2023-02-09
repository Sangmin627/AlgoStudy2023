import sys
input = sys.stdin.readline

n = int(input())
times = []
for i in range(n):
    start, end = map(int, input().split())
    times.append((start, end, i))
times.sort(key=lambda x: (x[0], x[1]))

visited = [0] * n
answer = 0

idx = 1
while sum(visited) != n:
    before_start, before_end, original_idx = times[idx - 1]
    next_start, next_end, next_original_idx = times[idx]
    visited[original_idx] = 1
    if not visited[next_original_idx]:
        if next_start >= before_end:
            idx += 1
        elif next_start < before_end:
            answer += 1
            times.append(times.pop(idx))
        visited[next_original_idx] = 1

print(answer if answer != 0 else 1)
