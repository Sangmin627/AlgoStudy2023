import sys

input = sys.stdin.readline
N = int(input())
arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

S = list(input().rstrip())
re_S = S[::-1]

print(S)
print(re_S)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if re_S[i - 1] != S[j - 1]:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
        elif re_S[i - 1] == S[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1

print("----- 정답 -----")
for a in arr:
    print(*a)
print()

print(N - arr[-1][-1])