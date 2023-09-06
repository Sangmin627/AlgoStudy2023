import sys
from collections import deque

input = sys.stdin.readline
r, s = map(int, input().split())
arr = [[0] for _ in range(r)]
visited = [[[] for _ in range(s)] for _ in range(r)]    # 방문 기록

for i in range(r):
    arr[i] = list(input().rstrip())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def hand(arr, x, y, flag):
    count = 0
    a_count = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < s:
            if arr[nx][ny] == 'o':
                count += 1
                if flag == 'o' and (x, y) not in visited[nx][ny]:
                    visited[x][y].append((nx, ny))
                    a_count += 1

    return count, a_count


max_value = 0
max_x, max_y = 0, 0 # 상근이가 최대한 많은 악수를 할 수 있는 자리 좌표
answer = 0  # 최종 답안

for x in range(r):
    for y in range(s):
        if arr[x][y] == '.':
            h, a = hand(arr, x, y, '.')
            if max_value < h:
                max_value = h
                max_x, max_y = x, y
        else:
            h, a = hand(arr, x, y, 'o')
            answer += a


arr[max_x][max_y] = 'o'
print(answer + max_value)

