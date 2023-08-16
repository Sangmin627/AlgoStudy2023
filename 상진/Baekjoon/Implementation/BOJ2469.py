import sys
input = sys.stdin.readline

K = int(input())
N = int(input())
target = list(input().rstrip())
g = []
for i in range(N):
    g.append(list(input().rstrip()))
    if g[i][0] == '?':
        hidden_layer = i

g += [target]

hidden_movable = [1] * (K-1) # 1 : *, 0 = -
hidden_candidates = [[] for _ in range(K)]

def check_and_go(y, x):
    move_candidates = [x, x - 1]
    flag = -1 # -1: 아래로, 0:오른쪽으로, 1:왼쪽으로
    for i in range(2):
        nx = move_candidates[i]
        if 0 <= nx < K - 1:
            if g[y][nx] == '-':
                flag = i
                break

    if flag == -1:
        y += 1
    elif flag == 0:
        x += 1
        y += 1
    else:
        x -= 1
        y += 1

    return y,x

not_target = []
for i in range(K):
    not_target.append(i)
    now = chr(65+i)
    y, x = 0, i
    while y < N:
        if y == hidden_layer:
            hidden_candidates[i] = [x, x-1] # 처음에는 * 이라고 가정, 그냥 내려감
            y += 1
            continue

        y,x = check_and_go(y, x)

    if g[y][x] == now:
        not_target.pop()
        for hc in hidden_candidates[i]:
            if 0 <= hc < K-1:
                hidden_movable[hc] = 0

for i in not_target:
    now = chr(65+i)
    y = hidden_layer
    sy = y
    for j in range(2):
        x = hidden_candidates[i][j] # 0 : 오른쪽, 1 : 왼쪽
        sx = x
        if 0 <= x < K-1 and hidden_movable[x]:
            g[y][x] = '-'
            if j == 0:
                y += 1
                x += 1
            else:
                y += 1
                x -= 1

            while y < N:
                y,x = check_and_go(y, x)

            if g[y][x] == now:
                hidden_movable[sx] = 0
                y = sy
            else:
                g[sy][sx] = '?' # 원복
                y = sy

ans = 0
for i in range(K):
    now = chr(65+i)
    y, x = 0, i
    while y < N:
        y,x = check_and_go(y, x)

    if g[y][x] == now:
        ans += 1

if ans == K:
    print("".join(g[hidden_layer]).replace("?", '*'))
else:
    print("x" * (K-1))