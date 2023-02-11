"""
- 직관적인 방법 : N x 10^9 개의 리스트를 만듦 -> 메모리 초과일거 같음
- 알고리즘 방법 : 최소..
1. 입력을 모두 받음 [(S_1, T_1), (S_2, T_2), (S_3, T_3), ...]
2. 정렬하면 시간이 빠른 수업부터 배치시킬 수 있음.
"""
import sys
import time

input = sys.stdin.readline
N = int(input())


start_0 = time.time()
Classes = []
for _ in range(N):
    s, t = map(int, input().split(' '))
    Classes.append((s, t))

end_0 = time.time()
print('0. 경과 시간 : ', (end_0 - start_0) * 100000)

start_1 = time.time()
# 정렬
Classes.sort()

end_1 = time.time()
print('1. 경과 시간 : ', (end_1 - start_1) * 100000)


start_2 = time.time()
# 시간이 빠른 수업 부터 배치 시작.
room = []
for Class in Classes:
    if not room:    # room 초기화
        room.append([Class])
        continue

    flag = False # 추가 됐는지 않 됐는지
    for i in range(len(room)):
        if Class[0] >= room[i][-1][1]:
            room[i].append(Class)
            flag = True
            break

    if not flag:
        room.append([Class])

end_2 = time.time()
print('2. 경과 시간 : ', (end_2 - start_2) * 100000)

print(room)
print(len(room))

