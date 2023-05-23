from itertools import product


def solution(users, emoticons):
    answer = []
    discount = [10, 20, 30, 40]

    # 이모티콘 할인 모든 경우의 수
    discount_list = list(product(discount, repeat=len(emoticons)))

    for discounts in discount_list:
        sub_cnt = 0
        buy_money = 0
        for user in users:
            buy = 0
            min_dis = user[0]
            max_money = user[1]

            for i in range(len(emoticons)):
                if min_dis > discounts[i]:
                    continue

                buy += emoticons[i] * (100 - discounts[i]) // 100
            if buy >= max_money:
                sub_cnt += 1
            else:
                buy_money += buy
        answer.append([sub_cnt, buy_money])
    answer.sort(key=lambda x: (x[0], x[1]))

    return answer[-1]