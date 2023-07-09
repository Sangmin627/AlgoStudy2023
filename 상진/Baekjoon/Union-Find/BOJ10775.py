import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
ans = 0
flag = True

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(P):
    d = int(input())
    root_d = find(d)
    if root_d != 0 and flag:
        parent[root_d] = root_d - 1
        ans += 1
    else:
        flag = False
        break

print(ans)
