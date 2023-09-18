def solution(begin, target, words):
    global answer, flag
    answer = 1000
    flag = False
    size = len(words)
    visited = [0] * size

    def check(now, next):
        cnt = len(now)
        for i in range(len(now)):
            if now[i] == next[i]:
                cnt -= 1

        if cnt != 1:
            return False
        return True

    def back(cnt, word):
        global answer, flag
        if word == target:
            answer = min(answer, cnt)
            flag = True
            return

        for i in range(size):
            if not visited[i]:
                if check(word, words[i]):
                    visited[i] = 1
                    cnt += 1
                    back(cnt, words[i])
                    cnt -= 1
                    visited[i] = 0

    back(0, begin)
    if not flag:
        return 0
    return answer