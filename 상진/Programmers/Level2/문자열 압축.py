def solution(s):
    s += "-"
    answer = 1001
    size = len(s)

    for i in range(1, size // 2 + 1):
        ans_tmp = ""
        idx = 0
        while idx < size - 1:
            now = s[idx:idx + i]
            cnt = 1
            while idx < size - 1:
                next = s[idx + i:idx + i + i]
                if next == now:
                    cnt += 1
                    idx += i
                    continue

                if cnt != 1:
                    ans_tmp += str(cnt) + now
                else:
                    ans_tmp += now
                idx += i
                break
        if "-" in ans_tmp:
            ans_tmp = ans_tmp[:-1]
        answer = min(len(ans_tmp), answer)

    return answer