import sys
recursion_limit = 10**9
sys.setrecursionlimit(recursion_limit)

input = sys.stdin.readline
N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
visited = [0] * N
answer = []
count = 0

def dfs(start_idx):
    global count

    if R < sum(answer):
        return

    if len(answer) >= 2:
        if L <= sum(answer) <= R and X <= (max(answer) - min(answer)):
            count += 1

    for i in range(start_idx, N):
        answer.append(problems[i])
        dfs(i + 1)
        answer.pop()


dfs(0)
print(count)