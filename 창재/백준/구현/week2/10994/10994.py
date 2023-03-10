
# n 일때 가로 세로 길이 구하는 함수
def high(n):
    if n == 0: return 1
    result = high(n-1) + 4
    return result


# 윗 줄부터 차례 대로..
def star(n, origin):
    # n = 0 일때, 즉 가운데 줄은 한번만 실행 되어야함.
    if n > 0:
        print('* ' * (origin - n) + '*' * high(n) + ' *' * (origin - n))
        print('* ' * (origin - n + 1) + ' ' * high(n - 1) + ' *' * (origin - n + 1))

    elif n < 0:
        print('* ' * (origin - abs(n) + 1) + ' ' * high(abs(n) - 1) + ' *' * (origin - abs(n) + 1))
        print('* ' * (origin - abs(n)) + '*' * high(abs(n)) + ' *' * (origin - abs(n)))

    else: print('* ' * (origin - n) + '*' * high(n) + ' *' * (origin - n))

    # 끝까지 다 돌았으면 stop
    if n == - origin:
        return 0
    else:
        star(n - 1, origin)  # return 하고 안하고 차이?


if __name__ == '__main__':
    n = int(input())
    h = high(n)

    # 위에서 계산할 때 편하게 하기 위해, 예를들어 3을 입력하면 2 1 0 -1 -2 로 하게끔
    # 이렇게 안하면 3 2 1 0 -1 이렇게 됨.
    star(n - 1, n - 1)