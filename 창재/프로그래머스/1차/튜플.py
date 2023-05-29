def solution(s):
    answer = []

    S = list(s.replace("{", ".").replace("}", ".").replace(",", "."))

    i = 0
    front_dot_flag = True
    memo = []
    while i < len(S):
        if front_dot_flag:
            if S[i] == '.':
                i += 1
                continue
            else:
                memo.append(S[i])
                i += 1
                front_dot_flag = False

        else:
            if S[i] == '.':
                answer.append(int(''.join(memo)))
                memo = []
                i += 1
                front_dot_flag = True
            else:
                memo.append(S[i])
                i += 1

    set_S = list(set(answer))
    a = sorted(set_S, key = lambda x: answer.count(x) , reverse = True)

    return a

s = "{{20,111},{111}}"
print(solution(s))