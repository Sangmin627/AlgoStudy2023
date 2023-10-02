# 이분탐색
# 파라메트릭 서치
def isPass(key, stones, k):
    check = 0

    for s in stones:
        if s < key:
            check += 1
        else:
            check = 0

        if check >= k:
            return False

    return True


def solution(stones, k):
    answer = 0

    keys = list(set(stones))
    keys.sort()
    # print("keys set = ", keys)

    start = 0
    end = len(keys) - 1
    mid = (end + start) // 2
    while end >= start:
        # print("keys[mid] = ", keys[mid])
        if isPass(keys[mid], stones, k):
            answer = keys[mid]
            start = mid + 1
            mid = (end + start) // 2
        else:
            end = mid - 1
            mid = (end + start) // 2
        # print("answer = ",answer)
    # print(answer)
    return answer