#
arr = []
for i in range(10):
	arr.append(list(map(int,input().split())))

bingo = arr[:5]
num = arr[5:]

#대각선, 1자 인 경우 빙고 생성 가능 > 대각선인 경우는 하나만 존재함
num_list= []
bingo_list = []
for i in range(5):
	for j in range(5):
		num_list.append(num[i][j])
		bingo_list.append(bingo[i][j])
bingo_test = [0 for _ in range(25)]

solution_list = []
for i in range(25):
	check = 0
	idx = bingo_list.index(num_list[i])
	bingo_test[idx] =1
	# 가로빙고
	for k in range(0,25,5):
		#k = 0,5,10,15,20
		# case_0,1,2,3,4
		globals()['case_'+str((k//5))]= bingo_test[0+k] + bingo_test[1+k] +bingo_test[2+k] + bingo_test[3+k] + bingo_test[4+k]
	# 세로빙고
	for j in range(0,5):
		# j = 0,1,2,3,4
		# case_5,6,7,8,9
		globals()['case_' + str(j+5)] = bingo_test[0 + j] + bingo_test[5 + j] + bingo_test[10 + j] + bingo_test[15 + j] + bingo_test[20 + j]

	# 대각선 빙고
	case_10 = bingo_test[0]+bingo_test[6]+bingo_test[12] +bingo_test[18] + bingo_test[24]
	case_11 = bingo_test[4]+bingo_test[8]+bingo_test[12] +bingo_test[16] + bingo_test[20]

	for var in range(12):
		if eval('case_' + str(var)) == 5:
			check += 1
			if check == 3 :
				solution_list.append(i)
				

print(min(solution_list)+1)
		

