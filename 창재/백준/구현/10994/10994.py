
# n 일때 가로 세로 길이 구하는 함수
def high(n):
    if n == 0: return 1
    result = high(n-1) + 4
    return result


def star(n, origin):
    if n >= 0:
        print('* ' * (origin - n) + '*' * high(n) + ' *' * (origin - n))

    elif n < 0:
        print('* ' * (origin - abs(n) + 1) + ' ' * high(abs(n) - 1) + ' *' * (origin - abs(n) + 1))

    if n > 0:
        print('* ' * (origin - n + 1) + ' ' * high(n - 1) + ' *' * (origin - n + 1))

    elif n < 0:
        print('* ' * (origin - abs(n)) + '*' * high(abs(n)) + ' *' * (origin - abs(n)))

    # 끝까지 다 돌았으면 stop
    if n == - origin:
        return 0
    else:
        star(n - 1, origin)


if __name__ == '__main__':
    n = int(input())
    h = high(n)

    # 위에서 계산할 때 편하게 하기 위해, 예를들어 3을 입력하면 2 1 0 -1 -2 로 하게끔
    # 이렇게 안하면 3 2 1 0 -1 이렇게 됨.
    star(n - 1, n - 1)

