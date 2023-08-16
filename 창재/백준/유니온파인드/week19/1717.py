# 1. 초기화 -> 인덱스 가 값 : 자기 자신이 대표.
# 2. union -> 대표 노드 끼리 연결 : 값을 대표 노드로 변경.
# 3. find -> 자신이 속한 집합의 대표 노드를 찾는 연산.
# 3.1 인덱스 와 값을 비교 -> 같으면 대표, 다르면 value 가 가리키 는 인덱스 로 이동.
# 3.2 대표 노드를 찾을 때 까지 재귀 반복. -> 찾으면 재귀를 벗어남.
# 4. 재귀를 빠져 나오면서 값들을 대표 노드로 업데이트 해줌.
# 5. 그래프 형태를 변경해 find 할때 시간 복잡도 를 줄임.

############### 문제 해석 ###############
# 0ab -> union(a, b)
# 1ab -> find(a) == find(b) -> YES or NO
# 작은 값을 대표로 한다.

import sys
limit_number = 100000
sys.setrecursionlimit(limit_number)

def find(a):
    if a == memo[a]:
        return a
    else:
        memo[a] = find(memo[a])
        return memo[a]


def union(a, b):
    f_a = find(a)
    f_b = find(b)
    super = min(f_a, f_b)  # 더 작은 값을 대표노드로 함.
    memo[f_a] = super  # 값을 대표 노드로 바꿔줌.
    memo[f_b] = super


input = sys.stdin.readline
n, m = map(int, input().split())

memo = [i for i in range(n + 1)]

for _ in range(m):
    x, a, b = map(int, input().split())

    if x == 0: # 0
        union(a, b)

    else: # 1
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")