# import sys
# sys.setrecursionlimit(10**6)
#
# input = sys.stdin.readline
# n, m, k = map(int, input().split())
#
# arr = [[0] * m for _ in range(n)]
#
# dx = [1, 0]
# dy = [0, 1]
#
#
# def dfs(sx, sy, ex, ey, c):
#     if sx == ex and sy == ey:
#         c += 1
#         return c
#
#     for i in range(2):
#         nx = sx + dx[i]
#         ny = sy + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             print("nx, ny = ", nx, ny)
#             c = dfs(nx, ny, ex, ey, c)
#             print("count = ", c)
#
#     return c
#
#
# def find_k(fk):
#     fx, fy = 0, 0
#     flag = False
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == fk:
#                 fx, fy = i, j
#                 # print("fx, fy = ", fx, fy)
#                 flag = True
#                 break
#         if flag:
#             break
#
#     return fx, fy
#
#
# if k == 0:
#     count = 0
#     count = dfs(0, 0, n-1, m-1, count)
#     print(count)
# else:
#     mx = k // m
#     my = k % m - 1
#     print(mx)
#     print(my)
#
#     count_f = 0
#     count_b = 0
#     count_f = dfs(0, 0, mx, my, count_f)
#     count_b = dfs(mx, my, n-1, m-1, count_b)
#
#     # print(count_f)
#     # print(count_b)
#     print(count_f * count_b)

import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

arr = [[1] * m for _ in range(n)]


def dp(sx, sy, x, y):
    for i in range(sx, x):
        for j in range(sy, y):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]


if k == 0:
    dp(1, 1, n, m)
    print(arr[n-1][m-1])
else:
    mx = (k - 1) // m
    my = k - (mx * m) - 1
    print(mx)
    print(my)

    dp(1, 1, mx + 1, my + 1)
    dp(mx + 1, my + 1, n, m)

    # print(arr[mx][my])
    # print(arr[n-1][m-1])
    print(arr[mx][my] * arr[n - 1][m - 1])