import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N,M = map(int, input().split())
parent = [i for i in range(N+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):
    op,s,e = map(int, input().split())
    if op == 0:
        union(s,e)
    else:
        if find(s) == find(e):
            print("YES")
        else:
            print("NO")