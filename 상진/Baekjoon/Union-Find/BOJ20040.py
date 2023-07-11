import sys
input = sys.stdin.readline

N,M = map(int, input().split())
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

ans = 0
for i in range(1,M+1):
    s,e = map(int, input().split())
    if find(s) == find(e):
        ans = i
        break
    else:
        union(s,e)

print(ans)