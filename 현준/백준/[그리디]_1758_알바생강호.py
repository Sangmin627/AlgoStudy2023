n = int(input())
customer = []
solution_list = []
# 배열로 고객을 받는다
for _ in range(n):
	customer.append(int(input()))
	solution_list.append(0)
# -100이든, -1 이든 받는 금액은 0원으로 똑같음
# 순서가 하나 밀릴수록 팁 금액은 -1이 됨
# 전체 - 의 수는 정해져 있음 ex) 처음 -0/ 두번째 -1/ 세번쪠 -2/ ....
# 따라서, 팁을 적게주는 고객을 뒤로 보내서 -를 최대화 해서 0 으로 만들어야함
customer.sort(reverse=True)
for i in range(len(customer)):
	tip = customer[i] - i
	if tip >= 0 :
		solution_list[i] = tip

print(sum(solution_list))