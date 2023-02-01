import sys

input = sys.stdin.readline

N = int(input())
stair = [0]
음
for i in range(N):
    stair.append(int(input()))

max_stair = [[] for _ in range(N + 1)]

def sumAll(N):
    sum = 0
    for j in max_stair[N]:
        sum += stair[j]
    return sum


for i in range(N + 1):
    if i == 0:
        continue
    elif i == 1:
        max_stair[1] = [1]
    elif i == 2:
        max_stair[2] = [1, 2]
    # elif i == 3:
    #     max_stair[3] = [2, 3]
    else:
        Max = sumAll(i - 3) + stair[i - 1]
        max_stair[i] += max_stair[i - 3] + [i - 1, i]

        if Max < sumAll(i - 2):
            Max = sumAll(i - 2)
            max_stair[i] = []
            max_stair[i] += max_stair[i - 2] + [i]


print(stair)
print(max_stair)

print(sumAll(N))