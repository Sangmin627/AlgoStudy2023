from itertools import product


def total_member_cul(users, emoticons, discount, emoticons_cnt):
    num_of_joined = 0
    total_sales = 0

    for u in users:
        total_price_m = 0
        for i in range(emoticons_cnt):
            if discount[i] >= u[0]:
                total_price_m += emoticons[i] * (1 - (discount[i] / 100))

        if total_price_m >= u[1]:
            num_of_joined += 1
        else:
            total_sales += total_price_m

    return num_of_joined, total_sales


def solution(users, emoticons):
    answer = [0, 0]

    # 할인률 종류
    kind_of_discount = [10, 20, 30, 40]

    # 이모티콘 개수
    emoticons_cnt = len(emoticons)

    # 이모티콘 개수만큼 할인율 중복 순열 -> 나올 수 있는 모든 경우의 수
    discount_product = list(product(kind_of_discount, repeat=emoticons_cnt))

    for discount in discount_product:
        # result = discount 일 때, [총 가입수, 총 판매액]
        result_joined, result_sales = total_member_cul(users, emoticons, discount, emoticons_cnt)

        if result_joined > answer[0]:
            answer = [result_joined, result_sales]

        elif result_joined == answer[0]:
            if result_sales > answer[1]:
                answer = [result_joined, result_sales]

    return answer