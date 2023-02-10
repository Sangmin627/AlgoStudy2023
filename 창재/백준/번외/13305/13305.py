"""
- 1km 당 기름 1L 사용
- 각 도시는 하나의 주유소를 가지고 있음. 주유소마다 리터당 가격이 다름.
-
"""
import sys

input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
distance.append(0)
price = list(map(int, input().split()))

print('distance : ', distance)
print('price : ', price)

min_value = price[0]
d = distance[0]
sum = 0

for i in range(1, N):
    if price[i] < min_value or i == (N - 1):
        sum += min_value * d
        min_value = price[i]
        d = distance[i]
    else:
        d += distance[i]

print(sum)