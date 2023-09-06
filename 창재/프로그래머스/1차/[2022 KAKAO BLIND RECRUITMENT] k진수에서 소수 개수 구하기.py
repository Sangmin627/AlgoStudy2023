def search_max_jalisu(n, k):
    i = 0
    while (k ** i) <= n:
        i += 1

    i -= 1
    return i


def transform(n, k):
    max_jalisu = search_max_jalisu(n, k)
    print(max_jalisu)

    result = [0] * (max_jalisu + 1)

    for i in range(max_jalisu, -1, -1):
        mok = n // (k ** i)
        result[max_jalisu - i] = mok
        n -= mok * (k ** i)

    return result


def sosu_check(value):
    if n == 1:
        return False

    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


def OPO(new_n):
    result = []
    flag = [False, -1]
    for i in range(len(new_n)):
        if new_n[i] == 0:
            if flag[0] == False:
                flag[0] = True
                flag[1] = i
            elif flag[0]:
                value = ''.join(list(map(str, new_n[flag[1] + 1:i - 1])))
                if sosu_check(value):
                    result.append(value)
                    flag[1] = i

    return result


def solution(n, k):
    answer = -1
    result = []

    new_n = transform(n, k)
    print(new_n)

    result += OPO(new_n)
    print(result)
    # result += PO(new_n)
    # result += OP(new_n)
    # result += P(new_n)

    return answer