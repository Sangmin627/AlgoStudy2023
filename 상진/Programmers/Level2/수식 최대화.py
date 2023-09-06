from itertools import permutations
import copy

def parse(expression):
    ops = []
    nums = []
    tmp = ""
    for i in expression:
        if i.isnumeric():
            tmp += i
        else:
            ops.append(i)
            nums.append(int(tmp))
            tmp = ""
    nums.append(int(tmp))
    return ops, nums

def calculate(op, copy_ops, copy_nums):
    idx = copy_ops.index(op)
    if op == '-':
        copy_nums[idx] -= copy_nums[idx + 1]
    elif op == '+':
        copy_nums[idx] += copy_nums[idx + 1]
    else:
        copy_nums[idx] *= copy_nums[idx + 1]

    copy_nums.pop(idx + 1)
    copy_ops.pop(idx)

def solution(expression):
    answer = 0
    ops = "+*-"
    perms = list(permutations(ops, 3))

    ops, nums = parse(expression)

    for perm in perms:
        op1, op2, op3 = perm[0], perm[1], perm[2]
        copy_nums = copy.deepcopy(nums)
        copy_ops = copy.deepcopy(ops)
        while copy_ops.count(op1) != 0:
            calculate(op1, copy_ops, copy_nums)
        while copy_ops.count(op2) != 0:
            calculate(op2, copy_ops, copy_nums)
        while copy_ops.count(op3) != 0:
            calculate(op3, copy_ops, copy_nums)
        answer = max(answer, abs(copy_nums[0]))
    return answer