import sys
input = sys.stdin.readline

N = int(input())
tree = list(map(int, input().split()))
ans = [[] for _ in range(N)]
idx = len(tree) // 2
ans[0].append(tree[idx])

left = tree[:idx]
right = tree[idx+1:]

def rec(root_idx, sub_tree, level):
    if level == N:
        return
    l, r = sub_tree[:root_idx], sub_tree[root_idx + 1:]
    root_idx = len(l) // 2

    ans[level].append(l[root_idx])
    ans[level].append(r[root_idx])

    rec(root_idx, l, level+1)
    rec(root_idx, r, level+1)

rec(idx, tree, 1)

for i in ans:
    print(*i)
