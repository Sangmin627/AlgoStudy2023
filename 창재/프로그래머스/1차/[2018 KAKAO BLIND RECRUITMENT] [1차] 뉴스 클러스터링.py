def two_slice(str):
    result = []
    alpha = []

    for i in range(len(str) - 1):
        alpha.append(str[i].upper() + str[i + 1].upper())

    for a in alpha:
        if a.isalpha():
            result.append(a)

    return result


def extract(c1, c2):
    result = []

    for c in c1:
        if c in c2:
            result.append(c)
            c2.remove(c)
            continue

    print(result)
    return result


def solution(str1, str2):
    answer = 0

    collection1 = two_slice(str1)
    print(collection1)
    collection2 = two_slice(str2)
    print(collection2)

    same_collection = extract(collection1, collection2)

    l_c1 = len(collection1)
    l_c2 = len(collection2)
    l_s = len(same_collection)

    if l_c1 + l_c2 == 0:
        return 65536

    answer = int((l_s / (l_c1 + l_c2)) * 65536)
    print(answer)

    return answer