import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [i for i in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = []
for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(N):
        if g[i][j] == 1:
            union(i,j)

schedules = list(map(int, input().split()))
p = parent[schedules[0]-1]

ans = True
for i in schedules:
    if parent[i-1] != p:
        ans = False
        break

if ans:
    print("YES")
else:
    print("NO")