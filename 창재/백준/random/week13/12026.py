import sys

input = sys.stdin.readline
n = int(input())
street = list(input())
BOJ = ["B", "O", "J"]
memo = [int(1e9)] * n
memo[0] = 0

for i in range(n):
    cur = BOJ.index(street[i])  # 현재 기준의 알파벳 인덱스
    for j in range(i + 1, n):
        if street[j] == BOJ[(cur + 1) % 3]:   # 다음 와야할 알파엣이면
            memo[j] = min(memo[j], memo[i] + (j - i) ** 2)

if memo[-1] == int(1e9):
    print(-1)
else:
    print(memo[-1])