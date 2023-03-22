import sys
input = sys.stdin.readline

N,K = map(int, input().split())
weights = list(map(int, input().split()))
visited = [0] * N

for i in range(N):
    weights[i] -= K

stack = []
ans = 0
def dfs():
    global ans
    if sum(stack) < 0:
        return
    if len(stack) == N:
        ans += 1
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            stack.append(weights[i])
            dfs()
            stack.pop()
            visited[i] = 0

dfs()
print(ans)