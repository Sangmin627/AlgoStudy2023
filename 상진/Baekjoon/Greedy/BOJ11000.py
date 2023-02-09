import sys
input = sys.stdin.readline

n = int(input())
times = []
for i in range(n):
    start, end = map(int, input().split())
    times.append((start, end, end-start))

times.sort(key=lambda x: (x[0], x[1], x[2]))
visited = [0] * n

def sim(startIdx):
    before_time = times[startIdx]
    for idx, nexts in enumerate(times):
        if not visited[idx]:
            next_start = nexts[0]
            before_end = before_time[1]
            if next_start == before_end:
                visited[idx] = 1
                sim(idx)

startIdx = 0
visited[0] = 1
sim(0)
answer = 1
for i in range(n):
    if not visited[i]:
        sim(i)
        answer += 1

print(answer)
