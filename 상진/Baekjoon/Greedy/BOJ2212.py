import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

arr = sorted(list(map(int, input().split())))

distances = []
for i in range(n-1):
    distances.append((arr[i+1] - arr[i], i))
distances.sort(reverse=True)
slices = sorted(distances[:k-1], key=lambda x: x[1])

answer = 0
left_idx = 0

if n >= k:
    for i in range(k-1):
        right_idx = distances[i][1]
        answer += arr[right_idx] - arr[left_idx]
        left_idx = right_idx + 1
    answer += arr[-1] - arr[left_idx]
print(answer)