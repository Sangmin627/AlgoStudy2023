import sys

input = sys.stdin.readline

n = int(input())
m = int(input())


def solution(s, arr, idx):
    nn = s * s
    for i in range(s):
        arr[idx + i][idx] = nn - i
        if s == 1:
            return

        arr[(s-1+idx) - i][s-1+idx] = (nn - 2*(s-1)) - i


    for j in range(1, s - 1):
        arr[s-1+idx][j+idx] = nn - (s-1) - j
        arr[idx][(s-1+idx) - j] = (nn - 3*(s-1)) - j

    idx += 1
    solution(s - 2, arr, idx)
    return


arr = [[0] * n for _ in range(n)]

solution(n, arr, 0)

for i in range(n):
    print(*arr[i])

for i in range(n):
    for j in range(n):
        if arr[i][j] == m:
            print(i+1, j+1)
            break