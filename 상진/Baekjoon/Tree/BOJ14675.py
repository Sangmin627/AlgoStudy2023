import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    s,e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

Q = int(input())
for _ in range(Q):
    t,k = map(int, input().split())
    if t == 1:
        if len(tree[k]) == 1:
            print("no")
        else:
            print("yes")
    else:
        print("yes")
