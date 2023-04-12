import sys, heapq
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops_counts = list(map(int, input().split()))
ops_list = ["+", "-", "*", "/"]

ops = dict()
for i in range(4):
    ops[ops_list[i]] = ops_counts[i]

stack = []
ans = nums[0]

def cal(op, next):
    global ans
    if op == "+":
        ans += next
    elif op == "-":
        ans -= next
    elif op == "*":
        ans *= next
    else:
        if ans < 0:
            ans = (abs(ans) // next) * -1
        else:
            ans //= next
    return ans

min_q = []
max_q = []

idx = 1
def back():
    global idx,ans
    if len(stack) == N-1:
        heapq.heappush(min_q, ans)
        heapq.heappush(max_q, -ans)
        return

    next_num = nums[idx]
    before_ans = ans

    for key in ops.keys():
        if ops[key] != 0:
            if idx <= N:
                ans = cal(key, next_num)
                stack.append(ops[key])
                ops[key] -= 1
                idx += 1
                back()
                ans = before_ans
                idx -= 1
                ops[key] += 1
                stack.pop()

back()
print(-max_q[0],min_q[0])