import sys
sys.setrecursionlimit(1000000)

def find(n): # 대표 노드를 찾음
    if n == parent[n]:
        return n
    else:
        parent[n] = find(parent[n])
        return parent[n]

def union(i, j): # a와 b의 대표 노트를 연결
    pi = find(i)
    pj = find(j)
    super = min(pi, pj)
    parent[pi] = super
    parent[pj] = super
    print("parent = ", parent)


input = sys.stdin.readline
N = int(input())
M = int(input())

parent = [i for i in range(N)]
for i in range(N):
    network = list(map(int, input().split()))
    for j in range(i + 1, N):
        if network[j] == 1:
            union(i, j)

root = list(map(int, input().split()))

print("최종: ", parent)
p = find(root[0] - 1)
for r in root:
    if p != find(r - 1):
        print("NO")
        sys.exit()

print("YES")