def star(n, origin):
    if n > 1:
        star(n - 1, origin)
    for i in range(origin):
        if i < origin - n:
            print(' ', end='')
        else:
            print('*', end='')
    print()

if __name__ == '__main__':
    n = int(input())

    star(n, n)

