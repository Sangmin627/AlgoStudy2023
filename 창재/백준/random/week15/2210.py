import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

arr = [[0] for _ in range(5)]

for i in range(5):
    arr[i] = list(map(int, input().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = [0] * 1000000

def back(x, y, memo):
    if len(memo) == 6:
        s = ''.join(map(str, memo))
        answer[int(s)] = 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            memo.append(arr[nx][ny])
            print("memo append = ", memo)
            back(nx, ny, memo)
            memo.pop()
            print("memo pop = ", memo)


for i in range(5):
    for j in range(5):
        memo = [arr[i][j]]
        back(i, j, memo)

print(sum(answer))