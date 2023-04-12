import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

max_value = max(arr)    # 최대값 찾기
h = []

for i in range(n):      # 최대값과 같은 인덱스 모두 찾기
    if arr[i] == max_value:
        h.append(i)

s, e = h[0], h[-1]      # 가장 앞 부분과 가장 끝 부분

if s == (n - 1) - e:
    print("X")
elif s < (n - 1) - e:   # 오른쪽이 더 많으면 홍
    print("R")
else:                   # 왼쪽이 더 많으면 청
    print("B")