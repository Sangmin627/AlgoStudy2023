import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    # coin = list(map(int, input().split()))
    coin = [int(x) for x in input().split()]    # 이게 더 빠름.
    money = int(input())

    answer = [0] * (money + 1)
    answer[0] = 1   # 누적 계산을 위해 초기화

    for c in coin:
        for i in range(c, money+1):
            answer[i] += answer[i - c]

    print(answer[money])
