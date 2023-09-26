def matching(banned, user):
    if len(banned) != len(user):
        return False

    for i in range(len(banned)):
        if banned[i] != '*':
            if banned[i] != user[i]:
                return False

    return True


def solution(user_id, banned_id):
    answer = set()
    answer_list = []

    def dfs(user_id, banned_id, s_b):

        if len(answer_list) >= len(banned_id):
            answer.add(tuple(sorted(answer_list)))
            return

        for b in range(s_b, len(banned_id)):
            for u in range(len(user_id)):
                if user_id[u] in answer_list:
                    continue

                if matching(banned_id[b], user_id[u]):  # 만약 일치하면
                    answer_list.append(user_id[u])
                    dfs(user_id, banned_id, b + 1)
                    answer_list.pop()

    dfs(user_id, banned_id, 0)

    return len(answer)