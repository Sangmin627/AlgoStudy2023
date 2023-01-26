def star(n):
    if n > 1:
        star(n - 1)
    for i in range(n):
        print('*', end='')
    print()

if __name__ == '__main__':
    n = int(input())

    star(n)

