if __name__ == '__main__':
    n = int(input())

    try:
        flag = False  # 이중 포문을 벗어나기 위한 flag
        # 5이 제일 많을 수록 최소가 됨으로, 작아지게 한다.
        # i, j가 0 까지 돌아야 함으로 ( , -1, -1)
        for i in range(n // 5, -1, -1):
            for j in range(n // 2, -1, -1):
                if n % ((i * 5) + (j * 2)) == 0:
                    print(i+j)
                    flag = True
                    break
            if flag == True: break
    # 예외 처리
    # 나머지가 0이 될 수 없을땐, i=0, j=0 가지 돌았는데 걸리지 않았다면 거스름돈을 줄 수 없다는 뜻.
    # 그때 n 을 0으로 나눌 수 없으므로, ZeroDivisionError Exception 발생.
    except(ZeroDivisionError):
        print(-1)