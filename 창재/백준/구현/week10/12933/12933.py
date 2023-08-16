duck = list(input())
d = ['q', 'u', 'a', 'c', 'k'] * 500

cnt = 0
while duck:
    i = 0
    j = 0

    while i < len(duck):
        if duck[i] == d[j]:
            duck.pop(i)
            j += 1
            print(duck)
        else:
            i += 1

    if d[j] != 'q' or j == 0:
        print(-1)
        exit()

    cnt += 1
    print(cnt, '마리!')

print(cnt)