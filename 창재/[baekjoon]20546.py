def Jun(j_cash, machineDuck):
    stock = 0  # 주식 수

    for day in machineDuck:
        if j_cash >= day:
            stock += j_cash // day
            j_cash -= (j_cash // day) * day

    print("준현이의 자산 : ", (stock * machineDuck[13]) + j_cash)
    return (stock * machineDuck[13]) + j_cash


def Sung(s_cash, machineDuck):
    stock = 0  # 주식 수
    up, down = 0, 0  # 주가 증감 카운트
    yesterday = 0  # 전일 주가

    for idx, today in enumerate(machineDuck):
        # 첫날은 건너뛰기
        if idx == 0:
            yesterday = today
            continue

        if today > yesterday:
            up += 1
            down = 0
        elif today < yesterday:
            up = 0
            down += 1
        else:
            up, down = 0, 0

        # 매수, >= : 다음날 더 떨어지면 또 살 수 있음
        if down >= 3:
            stock += s_cash // today  # 누적 주식 수
            s_cash -= (s_cash // today) * today  # 남은 현금 계산
        # 매도
        elif up == 3:
            s_cash += stock * today
            stock = 0

        yesterday = today

    print("성민이의 자산 : ", (stock * machineDuck[13]) + s_cash)
    return (stock * machineDuck[13]) + s_cash


if __name__ == '__main__':
    cash = int(input())
    MachineDuck = list(map(int, input().split()))

    final_Jun = Jun(cash, MachineDuck)  # 준현이의 최종 자산
    final_Sung = Sung(cash, MachineDuck)  # 성민이의 최종 자산

    if final_Jun > final_Sung:
        print("BNP")
    elif final_Jun < final_Sung:
        print("TIMING")
    else:
        print("SAMESAME")