from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        combs = []
        for order in orders:
            for comb in combinations(sorted(order), c):
                combs.append("".join(comb))
        order_counts = Counter(combs).most_common()

        if not order_counts or order_counts[0][1] < 2:
            continue

        max_count = order_counts[0][1]

        for order in order_counts:
            if order[1] < max_count:
                break
            answer.append(order[0])

    answer.sort()
    return answer