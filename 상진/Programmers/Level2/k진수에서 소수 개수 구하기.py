def translate(n, k):
    s = ""
    while n > 0:
        s += str(n % k)
        n //= k
    return s[::-1]


def isPrime(n):
    if n == 1:
        return False

    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    n = translate(n, k)

    for i in n.split("0"):
        if i == "":
            continue
        if isPrime(int(i)):
            answer += 1

    return answer