import sys
input = sys.stdin.readline

N = int(input())
left = [0] + list(map(int, input().split()))
right = [0] + list(map(int, input().split()))
memo = [[-1] * (N+2) for _ in range(N+2)]
memo[1][1] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if memo[i][j] != -1:
            memo[i + 1][j] = max(memo[i+1][j], memo[i][j])  # 왼쪽 버림
            memo[i + 1][j + 1] = max(memo[i + 1][j + 1], memo[i][j])  # 왼-오 둘다 버림
            if left[i] > right[j]:
                memo[i][j+1] = max(memo[i][j+1], memo[i][j] + right[j]) # 오른쪽만 버림 (점수획득)

ans = -1
for i in range(1, N+1):
    for j in range(1,N+1):
        ans = max(ans, memo[i][j])

print(ans)