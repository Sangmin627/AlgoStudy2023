def solution(sticker):

    N = len(sticker)
    if N < 4:
        return max(sticker)

    # -1번째 스티커를 쓰지 않는 경우
    dp1 = [0 for _ in range(N)]
    dp1[2] = sticker[0]

    for i in range(3, N - 1):
        front3 = sticker[i - 3] + dp1[i - 3]
        front2 = sticker[i - 2] + dp1[i - 2]
        dp1[i] = max(front3, front2)
    print(dp1)

    # 0번째 스티커를 쓰지 않는 경우
    dp2 = [0 for _ in range(N)]
    dp2[3] = sticker[1]

    for i in range(4, N):
        front3 = sticker[i - 3] + dp2[i - 3]
        front2 = sticker[i - 2] + dp2[i - 2]
        dp2[i] = max(front3, front2)
    print(dp2)

    answer1 = max(sticker[N - 2] + dp1[N - 2], sticker[N - 3] + dp1[N - 3])
    answer2 = max(sticker[N - 1] + dp2[N - 1], sticker[N - 2] + dp2[N - 2])
    answer = max(answer1, answer2)
    print(answer)

    return answer