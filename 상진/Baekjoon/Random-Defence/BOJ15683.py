import sys, copy
input = sys.stdin.readline

dy = [0,1,0,-1]
dx= [1,0,-1,0]

N,M = map(int, input().split())
g = []
cctvs = []
ans = 65

for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(M):
        if 1 <= g[i][j] <= 5:
            cctvs.append((g[i][j],i,j))

def get_move_case(op):
    if op == 1:
        return [[0],[1],[2],[3]]
    elif op == 2:
        return [[0,2], [1,3]]
    elif op == 3:
        return [[0,1],[1,2],[2,3],[3,0]]
    elif op == 4:
        return [[2,3,0], [3,0,1], [0,1,2], [1,2,3]]
    else:
        return [[0,1,2,3]]

def get_count(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    return cnt

def monitor(board,move,y,x):
    for i in move:
        ny = y
        nx = x
        while True:
            ny += dy[i]
            nx += dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] != 6:
                    board[ny][nx] = 7
                elif board[ny][nx] == 6:
                    break
            else:
                break

def back(idx,board):
    global ans
    print(idx, board)
    if idx == len(cctvs):
        cnt = get_count(board)
        ans = min(ans, cnt)
        return

    cctv = cctvs[idx]
    op = cctv[0]
    y, x = cctv[1], cctv[2]
    moves = get_move_case(op)
    tmp = copy.deepcopy(board)
    for move in moves:
        monitor(tmp,move,y,x)
        back(idx+1, tmp)
        tmp = copy.deepcopy(board)

back(0, g)
print(ans)
