# step2
def split(p):
    p = list(p)
    cnt1, cnt2 = 0, 0
    idx = 0

    while idx < len(p):
        if p[idx] == "(":
            cnt1 += 1
        else:
            cnt2 += 1
        idx += 1

        if cnt1 == cnt2:
            break

    u = p[:idx]
    v = p[idx:]
    return u, v

# step3
def is_right(u):
    stack = []
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False

    return True

def reverse(u):
    if len(u) == 2:
        return []
    for i in range(1, len(u) - 1):
        if u[i] == "(":
            u[i] = ")"
        else:
            u[i] = "("
    return u[1:-1]

def solution(p):
    if p == '':
        return ''

    u, v = split(p)

    if is_right(u):
        return "".join(u) + solution("".join(v))
    else:
        tmp = "(" + solution("".join(v)) + ")"
        u = reverse(u)

    return tmp + "".join(u)
