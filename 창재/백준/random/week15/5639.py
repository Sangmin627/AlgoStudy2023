import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
node = {1: int(input())}


def front(root, n):
    if n < node[root]:
        if node.get(2 * root):
            front(2 * root, n)
        else:
            node[2 * root] = n
    elif n > node[root]:
        if node.get((2 * root) + 1):
            front((2 * root) + 1, n)
        else:
            node[(2 * root) + 1] = n


while 1:
    # 왜지?
    try:
        front(1, int(input()))
    except:
        break


def back(root):
    if node.get(2 * root):
        back(2 * root)

    if node.get((2 * root) + 1):
        back((2 * root) + 1)

    print(node[root])


back(1)