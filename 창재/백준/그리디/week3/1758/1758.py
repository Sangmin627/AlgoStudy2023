import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    tips = [int(input().strip()) for _ in range(n)]

    # n = int(input)
    # tips = list(int(input()) for _ in range(n))

    tips.sort()
    tips.reverse()

    sum = 0
    for idx, tip in enumerate(tips):
        realTip = tip - idx
        if realTip >= 0:
            sum += realTip

    print(sum)
