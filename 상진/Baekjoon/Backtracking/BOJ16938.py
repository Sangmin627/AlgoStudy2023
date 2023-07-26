import sys
input = sys.stdin.readline

N,L,R,X = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = 0
stack = []

def back(idx):
    global ans
    if len(stack) > 1 and L <= sum(stack) <= R:
        if stack[-1] - stack[0] >= X:
            ans += 1

    for i in range(idx,N):
        stack.append(arr[i])
        back(i+1)
        stack.pop()

back(0)
print(ans)