pd = {}
c = {}

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        pd[pb] = pa
        c[pa] +=  c[pb]


def find(x):
     if x == pd[x]:
         return pd[x]

     px = find(pd[x])
     pd[x] = px
     return pd[x]

def solution():
    N = int(input())
    for _ in range(N):
        a, b = input().split()

        # initialize dictionary
        if a not in pd:
            pd[a] = a
            c[a] = 1

        if b not in pd:
            pd[b] = b
            c[b] = 1

        union(a, b)
        pa = pd[a]
        print("pd = ", pd)
        print("c = ", c)
        print(c[pa])

T = int(input())
for _ in range(T):
    solution()
    pd = {}