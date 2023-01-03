# 준현 > 바로 매수
# 성민 > 3일 상승시 바로 매도, 3일 하락시 바로 매수

money = int(input())
chart = list(map(int, input().split()))

# 준현 성민 모두 처음 같은 돈을 가지고 시작
jun_money = money
sung_money = money

# 준현 주식수, 성민 주식수 = 으로 세팅
jun_stock = 0
sung_stock = 0

for i in range(len(chart)):
	# 나눗셈의 몫이 1 이상일 경우 == 하나라도 구매가 가능한 경우
	num_jun = jun_money // chart[i]
	num_sung = sung_money // chart[i]
	# 준현이 사는 경우
	if num_jun >= 1:
		jun_stock = jun_stock+num_jun
		jun_money = jun_money - num_jun*chart[i]
	# 성민이 매수하는 경우 3번연속 하락일 때, 구매가 가능할 때
	if i >= 3 and (chart[i-3] > chart [i-2] > chart[i-1]) and num_sung >=1:
		sung_stock = sung_stock + num_sung
		sung_money = sung_money - num_sung*chart[i]
	# 성민이 매도하는 경우 3번연속 상승일때
	elif i >= 3 and (chart[i-3] < chart [i-2] < chart[i-1]):
		#전량매도
		sung_money = sung_money + sung_stock * chart[i]
		#잔여 주식 = 0
		sung_stock = 0

jun = jun_stock*chart[-1] + jun_money
sung = sung_stock*chart[-1] + sung_money

if jun > sung :
	print('BNP')
elif jun < sung :
	print('TIMING')
else :
	print('SAMESAME')

