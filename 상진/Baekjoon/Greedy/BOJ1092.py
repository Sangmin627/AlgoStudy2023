import sys
input = sys.stdin.readline

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)

m = int(input())
boxs = sorted(list(map(int, input().split())), reverse=True)

if cranes[0] < boxs[0]:
    print(-1)
    exit()

answer = 0
while boxs:
    for i in range(n):
        for j in range(len(boxs)):
            if cranes[i] >= boxs[j]:
                boxs.pop(j)
                break
    answer += 1
print(answer)