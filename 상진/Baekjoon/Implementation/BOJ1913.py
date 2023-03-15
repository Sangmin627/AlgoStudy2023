import sys
input = sys.stdin.readline

N = int(input())
VAL = int(input())

arr = [[0] * N for _ in range(N)]
arr[N//2][N//2] = 1

ans = dict()
ans[1] = [N//2+1, N//2+1]

val = N**2

def down(idx):
    global val
    x = idx
    for i in range(idx, N-idx):
        arr[i][x] = val
        ans[val] = [i+1, x+1]
        val -= 1

def right(idx):
    global val
    y = N-(idx+1)
    for i in range(idx+1, N-(idx+1)):
        arr[y][i] = val
        ans[val] = [y+1, i+1]
        val -= 1


def up(idx):
    global val
    x = N-(idx+1)
    for i in range(N-(idx+1), idx-1, -1):
        arr[i][x] = val
        ans[val] = [i+1, x+1]
        val -= 1


def left(idx):
    global val
    y = idx
    for i in range(N-(idx+2), idx, -1):
        arr[y][i] = val
        ans[val] = [y+1, i+1]
        val -= 1

for i in range(N//2):
    down(i)
    right(i)
    up(i)
    left(i)

for i in range(N):
    print(*arr[i])
print(*ans[VAL])