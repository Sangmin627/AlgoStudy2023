from itertools import permutations


def seperation(expression):
    tmp = []
    operator = ["-", "+", "*"]
    used_operator = set()
    point = 0

    for i in range(len(expression)):
        if expression[i] in operator:
            tmp.append(int(expression[point:i]))
            tmp.append(expression[i])
            used_operator.add(expression[i])
            point = i + 1

    tmp.append(int(expression[point:]))

    return tmp, list(used_operator)


def calculator(expression, permut):
    for p in permut:
        tmp = []
        i = 0
        while i < len(expression):
            if expression[i] == p:
                if p == '-':
                    tmp[-1] -= expression[i + 1]
                elif p == '+':
                    tmp[-1] += expression[i + 1]
                else:
                    tmp[-1] *= expression[i + 1]

                i += 2

            elif expression[i] != p:
                tmp.append(expression[i])
                i += 1

        expression = tmp
        print("expression = ", expression)

    return abs(expression[0])


def solution(expression):
    expression, operator = seperation(expression)

    permutation = list(permutations(operator, len(operator)))

    max_value = 0
    for permut in permutation:
        max_value = max(max_value, calculator(expression, permut))

    return max_value