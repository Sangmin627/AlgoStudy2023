import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
        friends[a] += friends[b]
    elif a > b:
        parent[a] = b
        friends[b] += friends[a]

T = int(input())
for _ in range(T):
    N = int(input())
    dic = dict()
    parent = []
    friends = []
    idx = 0
    for _ in range(N):
        s,e = map(str, input().split())
        if s not in dic.keys():
            dic[s] = idx
            parent.append(idx)
            friends.append(1)
            idx += 1
        if e not in dic.keys():
            dic[e] = idx
            parent.append(idx)
            friends.append(1)
            idx += 1

        union(dic[s], dic[e])
        print(friends[find(dic[s])])


