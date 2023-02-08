import sys
input = sys.stdin.readline

globalString = list(input().rstrip())
string = globalString
size = len(string)
visited = [0] * size

def recursion(start, string):
    if not string:
        return
    now = sorted(string)[0]
    idx = string.index(now)

    visited[start + idx] = 1
    for i in range(size):
        if visited[i] == 1:
            print(globalString[i],end="")
    print()

    right = string[idx+1:]
    left = string[:idx]
    recursion(start+idx+1, right)
    recursion(start, left)

recursion(0, string)