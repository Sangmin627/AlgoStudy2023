import sys

input = sys.stdin.readline
N, M = map(int, input().split())

arr = [0 for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, list(input().rstrip())))

max_value = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            if i > 0 and j > 0:
                arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1

            if arr[i][j] > max_value:
                max_value = arr[i][j]

print(max_value**2)
