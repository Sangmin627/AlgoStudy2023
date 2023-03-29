import sys

input = sys.stdin.readline
n, m = map(int, input().split())
naming = []
him = []

for i in range(n):
    a, b = input().split()
    # if int(b) not in him: 어이가 없네
    naming.append(a)
    him.append(int(b))
    # else:
    #     n -= 1

print(naming)
print(him)


def binary_search_right(t):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if t > him[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return start


for _ in range(m):
    v = int(input())
    locate = binary_search_right(v)
    print(naming[locate])