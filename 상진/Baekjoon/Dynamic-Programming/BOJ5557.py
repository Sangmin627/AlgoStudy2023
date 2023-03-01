N = int(input())
nums = list(map(int, input().split()))

memo = [[0] * 21 for _ in range(N-1)]
memo[0][nums[0]] = 1

for i in range(1,N-1):
    for j in range(21):
        if memo[i-1][j] != 0:
            if j + nums[i] <= 20:
                memo[i][j + nums[i]] += memo[i-1][j]
            if j - nums[i] >= 0:
                memo[i][j - nums[i]] += memo[i-1][j]

print(memo[-1][nums[-1]])