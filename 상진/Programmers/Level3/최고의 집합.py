def solution(n, s):
    answer = []
    if n > s:
        return [-1]

    while n > 0:
        answer.append(s // n)
        s -= s // n
        n -= 1

    return answer