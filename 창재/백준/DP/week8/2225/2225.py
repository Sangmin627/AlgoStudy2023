import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [[0 for _ in range(k + 1)] for _ in range(n + 1)]


def sol(a, b):
    if b == 1:
        arr[a][b] = 1
        return

    for i in range(a + 1):
        if arr[i][b - 1] == 0:  # 값이 채워 지지 않았다면
            sol(i, b - 1)       # 채우기 부터

        arr[a][b] += arr[i][b - 1]  # 그 다음에 누적 합


sol(n, k)

for i in range(n + 1):
    print(*arr[i])
    print()

print(arr[n][k] % 1000000000)
