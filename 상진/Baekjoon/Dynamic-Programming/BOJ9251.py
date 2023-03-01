import sys
input = sys.stdin.readline

s1 = "-"+input().rstrip()
s2 = "-"+input().rstrip()

size1 = len(s1)
size2 = len(s2)

memo = [[0] * size2 for _ in range(size1)]

for i in range(1, size1):
    for j in range(1,size2):
        if s1[i] == s2[j]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])

print(memo[size1-1][size2-1])

