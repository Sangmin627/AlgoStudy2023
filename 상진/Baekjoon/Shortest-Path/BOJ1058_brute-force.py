import sys
input = sys.stdin.readline

N = int(input())
friends = [[] for _ in range(N)]
ans = 0

for i in range(N):
    arr = input().rstrip()
    for j in arr:
        if j == "N":
            friends[i].append(0)
        else:
            friends[i].append(1)

for i in range(N):
    tmp = set()
    ff = []
    for j in range(N):
        if friends[i][j] == 1:
            tmp.add(j)
            ff.append(j)

    for f in ff:
        for k in range(N):
            if i != k:
                if friends[f][k] == 1:
                    tmp.add(k)
    ans = max(ans, len(tmp))

print(ans)