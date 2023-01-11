n = int(input())

answer = 0
while n > 1:
    if n % 5 != 0:
        n -= 2
        answer += 1
    else:
        n -= 5
        answer += 1

if n == 0:
    print(answer)
else:
    print(-1)