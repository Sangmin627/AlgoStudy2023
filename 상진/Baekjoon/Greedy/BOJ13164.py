import sys
input = sys.stdin.readline

n,k = map(int, input().split())
heights = list(map(int, input().split()))
answer = 0

slices = []
for i in range(n-1):
    slices.append((heights[i+1] - heights[i], i))
slices.sort(reverse=True)
slices = sorted(slices[:k-1], key=lambda x: x[1])

left_idx = 0
for i in range(k-1):
    right_idx = slices[i][1]
    answer += heights[right_idx] - heights[left_idx]
    left_idx = right_idx + 1
answer += heights[-1] - heights[left_idx]
print(answer)