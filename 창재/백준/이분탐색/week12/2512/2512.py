import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)


def total_budget(budget, upper):
    total = 0
    for b in budget:
        if b <= upper:
            total += b
        else:
            total += upper
    print("total: ", total)
    return total


def bianry_search(arr, budget, start, end, total):
    mid = (start + end) // 2
    print(mid)

    if total_budget(budget, mid) == total:
        print(mid)
        exit()

    elif total_budget(budget, mid) < total:
        if total_budget(budget, mid + 1) > total:
            print(mid)
            exit()

        bianry_search(arr, budget, mid + 1, end, total)

    elif total_budget(budget, mid) > total:
        bianry_search(arr, budget, start, mid - 1, total)

input = sys.stdin.readline
# 입력을 받고
n = int(input())
budget = list(map(int, input().split()))
total = int(input())

# 시작은 total // n 로 한다. 왜냐하면 total // n 보다 작게 하면 총 예산 값이 최대가 될 수 없다.
start = total // n
end = max(budget)

if end <= start:
    print(end)
    exit()

if sum(budget) <= total:
    print(end)
    exit()

arr = []

for i in range(start, end + 1):
    arr.append(i)

bianry_search(arr, budget, start, end, total)
