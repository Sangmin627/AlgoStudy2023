import sys
input = sys.stdin.readline

def init_prime():
    m = int(MAX ** 0.5)
    for i in range(2, m+1):
        if is_prime[i]:
            for j in range(i+i, MAX, i):
                is_prime[j] = False

def back(stack, s):
    global ans
    if stack:
        num = int("".join(stack))
        if num >= 2 and num not in ans_set:
            if is_prime[num]:
                ans_set.add(num)
                ans += 1

    for i in range(len(s)):
        if not visited[i]:
            stack.append(s[i])
            visited[i] = True
            back(stack, s)
            visited[i] = False
            stack.pop()

T = int(input())
MAX = 10 ** 7
is_prime = [True] * MAX
init_prime()
for _ in range(T):
    s = input().rstrip()
    ans = 0
    stack = []
    ans_set = set()
    visited = [False] * len(s)
    back(stack, s)
    print(ans)