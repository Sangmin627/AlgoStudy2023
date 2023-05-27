def translate(i, n, dic):
    s = []
    while i > 0:
        s += dic[i % n]
        i //= n

    return s[::-1]


def cul(n, t, m, dic):
    s = [0]  # 0일때 계산 안하기 위해 0으로 초기화
    i = 1
    while len(s) < t * m:
        s += translate(i, n, dic)
        i += 1

    return s[:t * m]


def tube(m, t, p, all_jinsu):
    s = ''
    for i in range(t):
        s += str(all_jinsu[(m * i) + (p - 1)])

    return s


def solution(n, t, m, p):

    dic = {i: str(i) for i in range(10)}
    al = list("ABCDEF")
    dic2 = {i + 10: al[i] for i in range(6)}
    dic.update(dic2)
    print("dic", dic)

    all_jinsu = cul(n, t, m, dic)
    print("all_jinsu", all_jinsu)   # 필요한데 까지만 진수 리스트 구하는 메소드

    answer = tube(m, t, p, all_jinsu)   # 튜브꺼만 골라주는 메소드
    print("answer", answer)

    return answer


solution(2, 4, 2, 1)