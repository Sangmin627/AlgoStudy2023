from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    size = len(banned_id)
    perms = list(permutations(user_id, size))

    def check(perm):
        for i in range(size):
            tmp_size = len(banned_id[i])
            if len(perm[i]) != tmp_size:
                return
            for j in range(tmp_size):
                if banned_id[i][j] == '*':
                    continue
                if banned_id[i][j] != perm[i][j]:
                    return

        perm = sorted(perm)
        if perm not in answer:
            answer.append(perm)
        return

    for perm in perms:
        check(perm)

    return len(answer)