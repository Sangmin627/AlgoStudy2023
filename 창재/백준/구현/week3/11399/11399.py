import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input().strip())    # 5
    P = list(map(int, input().split()))
    P.sort()

    # global SUM # 안되넹
    # (5 * P_1) + (4 * P_2) + (3 * P_3) + (2 * P_4) + (1 * P_5)
    SUM = 0
    for i in range(N):
        SUM += (N - i) * P[i]

    print(SUM)