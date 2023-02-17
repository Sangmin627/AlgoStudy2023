"""
- 직관적인 방법 : N x 10^9 개의 리스트를 만듦 -> 메모리 초과
- 알고리즘 방법 : 최소..
1. 입력을 모두 받음 [(S_1, T_1), (S_2, T_2), (S_3, T_3), ...]
2. 정렬하면 시간이 순서대로 맨 뒤 값만 참조하여 배치시킬 수 있음.
3. 최악 : O(N^2)..
"""
import sys
import time

input = sys.stdin.readline
N = int(input())

Classes = [0] * N

for i in range(N):
    s, t = map(int, input().split(' '))
    Classes[i] = (s, t)
    print(Classes)

# 정렬
Classes.sort()
print(Classes)

cnt = 0
while Classes:  # 리스트 가 빌때 까지
    i = 1
    init = Classes[0][1]
    cnt += 1

    while i < N:    # Classes 를 처음 부터 끝까지 돌겠다는 의미.
        if Classes[i][0] >= init:   # 다음 수업의 시작이 앞 수업의 끝보다 같거나 크면,
            init = Classes[i][1]    # 새로 임명. 그리고 pop
            Classes.pop(i)
            print(i, '인덱스 pop : ', Classes)
            N -= 1  # i 는 그대로 냅두고, 총 길이(N)를 줄임. pop 하면서 인덱스가 하나씩 당겨지니까.
        else:
            i += 1  # 다음 수업의 시작이 앞 수업의 끝보다 작으면, 다음 수업으로 넘어감.

    Classes.pop(0)
    N -= 1

print(cnt)

# 시간이 빠른 수업 부터 배치 시작.
room = []
for Class in Classes:
    if not room:    # room 초기화
        room.append([Class])
        # cnt += 1
        continue

    flag = False # 추가 됐는지 않 됐는지
    for i in range(len(room)):
        if Class[0] >= room[i][-1][1]:
            room[i].append(Class)
            flag = True
            break

    if not flag:
        room.append([Class])

# print(room)
# print(len(room))

