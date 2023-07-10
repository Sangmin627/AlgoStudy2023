# 1. 입력을 받는다.
# 2. 두 친구의 값을 모두 대표 값으로 바꾼다.
# 3. 두 친구의 대표값과 같은 값을 가진 친구들의 수를 센다.
# 4. 반복한다.

import sys
limit_number = 300000
sys.setrecursionlimit(limit_number)

def nameToIdx(name):
    global count_name

    if name not in dict_name:
        dict_name[name] = count_name
        memo.append(count_name)
        friend.append(1)
        count_name += 1
        return dict_name[name]

    return dict_name[name]

def union(x, y):
    f_x = find(x)
    f_y = find(y)
    memo[f_y] = f_x

    friend[f_x] += friend[f_y]

    return f_x

def find(x):
    if x == memo[x]:
        return memo[x]

    memo[x] = find(memo[x])
    return memo[x]


input = sys.stdin.readline
numOfTest = int(input())

for _ in range(numOfTest):
    numOfRelation = int(input())
    dict_name = {}
    memo = [0]
    friend = [0]
    count_name = 1

    for _ in range(numOfRelation):
        a, b = map(str, input().split())
        a_idx = nameToIdx(a)
        b_idx = nameToIdx(b)

        f_a = find(a_idx)
        f_b = find(b_idx)
        if f_a != f_b:
            super = union(a_idx, b_idx)
            print(friend[super])
        else:
            print(friend[f_a])
