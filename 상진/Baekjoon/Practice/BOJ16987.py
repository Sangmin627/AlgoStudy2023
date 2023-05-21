import sys
input = sys.stdin.readline

N = int(input())
E = [list(map(int, input().split())) for _ in range(N)]

def back(idx):
    global ans, cnt
    if idx == N:
        ans = max(ans, cnt)
        return
    if E[idx][0] <= 0:
        back(idx + 1)
        return
    if cnt == N-1:
        back(idx + 1)
        return

    for i in range(N):
        if i != idx and E[i][0] > 0:
            E[idx][0] -= E[i][1]
            E[i][0] -= E[idx][1]
            if E[idx][0] <= 0:
                cnt += 1
            if E[i][0] <= 0:
                cnt += 1
            back(idx+1)
            if E[idx][0] <= 0:
                cnt -= 1
            if E[i][0] <= 0:
                cnt -= 1
            E[idx][0] += E[i][1]
            E[i][0] += E[idx][1]

ans = 0
cnt = 0
back(0)
print(ans)
