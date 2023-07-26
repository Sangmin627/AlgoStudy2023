import sys
input = sys.stdin.readline

N = int(input())
ans = []
stack = []
def back():
    if len(stack) > 0:
        s = int("".join(list(map(str, stack))))
        ans.append(s)

    for i in range(10):
        if len(stack) == 0 or stack[-1] > i:
            stack.append(i)
            back()
            stack.pop()

back()
ans.sort()
if len(ans) >= N:
    print(ans[N-1])
else:
    print(-1)
