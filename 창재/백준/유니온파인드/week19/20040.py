# 1. 초기화 -> 인덱스 가 값 : 자기 자신이 대표.
# 2. union -> 대표 노드 끼리 연결 : 값을 대표 노드로 변경.
# 3. find -> 자신이 속한 집합의 대표 노드를 찾는 연산.
# 3.1 인덱스 와 값을 비교 -> 같으면 대표, 다르면 value 가 가리키 는 인덱스 로 이동.
# 3.2 대표 노드를 찾을 때 까지 재귀 반복. -> 찾으면 재귀를 벗어남.
# 4. 재귀를 빠져 나오면서 값들을 대표 노드로 업데이트 해줌.
# 5. 그래프 형태를 변경해 find 할때 시간 복잡도 를 줄임.

import sys
limit_number = 500000 # n <= 500,000 이므로
sys.setrecursionlimit(limit_number)


# 재귀 -> 960 ms
# def find(a):
#     if a == memo[a]:
#         return a
#     else:
#         memo[a] = find(memo[a])
#         return memo[a]

# 반복문 -> 648 ms
def find(a):
    while a != memo[a]:
        memo[a] = memo[memo[a]]
        a = memo[a]
    return memo[a]


input = sys.stdin.readline
n, m = map(int, input().split())

memo = [i for i in range(n)]

for i in range(1, m + 1):
    a, b = map(int, input().split())

    fa = find(a)
    fb = find(b)
    if fa == fb:
        print(i)
        sys.exit()

    memo[fa] = fb

print(0)