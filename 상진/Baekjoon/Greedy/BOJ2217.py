n = int(input())
ropes = list(int(input()) for _ in range(n))
ropes.sort()

answer = 0
idx = n
while idx > 0:
    tmp = idx * ropes[n-idx]
    answer = max(answer, tmp)
    idx -= 1

print(answer)