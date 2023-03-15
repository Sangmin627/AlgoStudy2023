import sys
input = sys.stdin.readline

N = int(input())
ans = N

for i in range(N):
    word = input().rstrip()
    for j in range(1, len(word)):
        if word[j-1] != word[j]:
            if word[j-1] in word[j+1:]:
                ans -= 1
                break

print(ans)

