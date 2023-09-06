# import sys
#
# input = sys.stdin.readline
# G = int(input())
# P = int(input())
# memo = [0] * (G + 1)
# count = 0
#
# for k in range(P):
#     q = int(input())
#     print("q = ", q)
#
#     if memo[q] + 1 <= q:
#         if count < G:
#             for i in range(q, G + 1):
#                 memo[i] += 1
#
#             count += 1
#             print("k =", k, " memo =", memo)
#             print("k =", k, " count =", count)
#             print()
#         else:
#             break
#     else:
#         break
#
# print("최종 memo = ", memo)
# print("최종 count = ", count)
# print(count)

import sys
sys.setrecursionlimit(10**5) # RecursionError 방지
input = sys.stdin.readline

G = int(input()) # 게이트
P = int(input()) # 비행기
parent = [i for i in range(G+1)] # 초기 각 게이트의 부모는 자기 자신
ans = 0
flag = True # flag 없이 break로 한다면 90% 대에서 틀렸습니다 발생

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(P):
    d = int(input())
    root_d = find(d)
    if root_d != 0:
        parent[root_d] = root_d - 1
        ans += 1
    else:
        break

print(ans)