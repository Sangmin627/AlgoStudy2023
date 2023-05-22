import sys
input = sys.stdin.readline

dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,-1,0,1,1,-1,1,-1]
R,S = map(int, input().split())
arr = []
empty_seat = []
cnt = 0

def check(sy,sx):
    cnt = 0
    for i in range(8):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= ny < R and 0 <= nx < S:
            if arr[ny][nx] == "o":
                cnt += 1
    return cnt

for i in range(R):
    arr.append(list(map(str, input().rstrip())))
    for j in range(S):
        if arr[i][j] == ".":
            empty_seat.append((i,j))

if len(empty_seat) != 0:
    for y,x in empty_seat:
        arr[y][x] = "o"
        tmp = 0
        for i in range(R):
            for j in range(S):
                if arr[i][j] == "o":
                    tmp += check(i,j)
        cnt = max(cnt, tmp//2)
        arr[y][x] = "."
    print(cnt)
else:
    for i in range(R):
        for j in range(S):
            cnt += check(i,j)
    print(cnt // 2)