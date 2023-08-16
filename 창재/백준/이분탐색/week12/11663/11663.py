import sys

input = sys.stdin.readline
n, m = map(int, input().split())
spot = list(map(int, input().split()))
spot.sort()


def binary_search_right(t):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if t > spot[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return end + 1


def binary_search_left(t):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if t >= spot[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return end


for _ in range(m):
    s, e = map(int, input().split())
    s_location = binary_search_right(s)
    e_location = binary_search_left(e)

    print(e_location - s_location + 1)
