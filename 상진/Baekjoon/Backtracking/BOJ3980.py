import sys
input = sys.stdin.readline

def back(idx):
    global ans
    if len(stack) == 11:
        ans = max(ans, sum(stack))
        return

    for i in range(11):
        if scores[idx][i] != 0 and not visited[i]:
            visited[i] = 1
            stack.append(scores[idx][i])
            back(idx+1)
            stack.pop()
            visited[i] = 0

T = int(input())
for _ in range(T):
    scores = [list(map(int, input().split())) for _ in range(11)]
    ans = 0
    stack = []
    visited = [0] * 11
    back(0)
    print(ans)
