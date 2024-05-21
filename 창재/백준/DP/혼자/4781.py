# 1 <= n <= 5,000
# 1 <= 100*m <= 10,000

while 1:
    n, m = map(float, input().split())
    n = int(n)
    m = int(m * 100)
    if n == 0 and m == 0:
        break

    dp = [0 for _ in range(m + 1)]

    for _ in range(n):
        c, p = map(float, input().split())
        c = int(c)
        p = int(p * 100)

        for i in range(p, m + 1):
            dp[i] = max(dp[i], dp[i - p] + c)

        print(dp)

    print(dp[m])

    #
    # dp = {0.0: 0}
    #
    # for _ in range(n):
    #     c, p = map(float, input().split())
    #     c = int(c)
    #
    #     max_m = int(m // p)
    #
    #     for i in range(max_m, 0, -1):
    #         cur_money = p * i
    #
    #         temp = {}
    #         for money, kal in dp.items():
    #             print("money + cur_money = ", money + cur_money)
    #             if money + cur_money <= m:
    #                 if money + cur_money not in dp:
    #                     temp[money + cur_money] = dp[money] + c * i
    #                 else:
    #                     temp[money + cur_money] = max(dp[money + cur_money], dp[money] + c * i)
    #
    #         dp.update(temp)
    #         print(dp)
    #
    # print(max(dp.values()))