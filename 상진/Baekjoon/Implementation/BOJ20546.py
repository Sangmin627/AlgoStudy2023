inputMoney = int(input())
dailyPrice = list(map(int, input().split()))

jhMoney, smMoney = inputMoney, inputMoney
jhStock, smStock = 0, 0

startPrice = dailyPrice[0]
cnt = 0

for price in dailyPrice:
    if jhMoney >= price:
        jhStock += jhMoney // price
        jhMoney -= jhStock * price

for price in dailyPrice[1:]:
    if price > startPrice:
        if cnt <= 0:
            cnt = 1
        else:
            cnt += 1
        startPrice = price
    elif price < startPrice:
        if cnt >= 0:
            cnt = -1
        else:
            cnt -= 1
        startPrice = price
    else:
        cnt = 0

    # 전량 매수
    if cnt <= -3:
        if smMoney >= price:
            buyableStock = smMoney // price
            smMoney -= buyableStock * price
            smStock += buyableStock

    # 전량 매도
    if cnt >= 3:
        smMoney += smStock * price
        smStock = 0

jhMoney = jhMoney + jhStock * dailyPrice[-1]
smMoney = smMoney + smStock * dailyPrice[-1]

if jhMoney > smMoney:
    print("BNP")
elif jhMoney == smMoney:
    print("SAMESAME")
else:
    print("TIMING")
