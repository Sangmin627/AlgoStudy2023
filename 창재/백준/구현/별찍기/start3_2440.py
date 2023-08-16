def star(n):
    for i in range(n):
        print('*', end='')
    print()
    if n > 1:
        star(n - 1)

if __name__ == '__main__':
    n = int(input())

    star(n)

