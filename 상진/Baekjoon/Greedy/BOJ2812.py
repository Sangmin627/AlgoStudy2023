import sys
input = sys.stdin.readline

N,K = map(int, input().split())
nums = list(map(int, input().rstrip()))
stack = []

for i in range(N):
    while stack and K != 0:
        if stack[-1] < nums[i]:
            stack.pop()
            K -= 1
        else:
            break
    stack.append(nums[i])

for i in range(K):
    stack.pop()

for i in stack:
    print(i, end="")
