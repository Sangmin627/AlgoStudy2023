"""
- 시간이 최소화 되려면, 마지막을 제외하고는 모든 크레인이 동시에 움직이는게 좋음.
- 그렇게 하려면 박스들의 무게를 기준으로, 크레인의 제한 무게를 기준으로 나누면 됨.
- 박스 수 : N , 크레인 수 : K 일 때,

1. 각 범위 마다 갯수를 계산
2. 가장 큰 갯수를 찾음
3. 그거보다 무게가 큰 애들 다 더한 다음에 평균값을 찾음
4. 그 평균값에 + 1 한게 정답.

- 같은 무게가 있을 수 있음. 얘넨, 같은 개수 만큼 나눠줌.
"""
import sys

input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split(' ')))

M = int(input())
boxes = list(map(int, input().split(' ')))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
print('cranes : ', cranes)
print('boxes : ', boxes)

if cranes[0] < boxes[0]:
    print(-1)
    exit()

answer = 0

while boxes:
    for crane in cranes:
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    answer += 1

print(answer)