# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

# 3번조건 > 행이 가장 작은 경우, 열이 가장 작은 경우 이므로
# 행이 가장 작은것 부터 돌고, 열이 가장 작은 것 부터 돌아야함
# 1번 조건 > 2차원 배열을 돌면서 주변의 친구가 몇명 있는지 계산, 위치 저장
# 2번 조건 > 1번을 만족하는 칸을 돌면서 빈자리 개수 계산, 위치 저장
# 3번 조건 > 행이 가장 작은칸, 번호가 자장 작은칸 자리 정하기
# 1번 > 2번 > 3번 순으로 진행

from collections import defaultdict


n = int(input())
num = n**2

student = {}
desk = [[0 for _ in range(n)]for _ in range(n)]

for i in range(num):
	arr = list(map(int,input().split()))
	student[arr[0]] = arr[1:]

#-------------------여기까지 입력----------------------------------------

# 각각의 학생마다 for문을 돌린다

# 상 하 좌 우
nx = [0,0,-1,1] # 좌우 >> col과 관련
ny = [-1,1,0,0] # 상하 >> row와 관련

for stu in student:

	
	# stu -- 학생
	like = student[stu]
	one = {} # 1번 조건을 저장할 배열
	two = {} # 2번 조건을 저장할 배열
	three = {} # 3번 조건을 저장할 배열
	
	
# ----1번조건--------
	# 2차원 배열을 돌면서
	for row in range(n):
		for col in range(n):
			one_cnt = 0
			# 주변에 친구가 몇명 있는지 찾기
			for i in range(4):
				dx = col + nx[i]
				dy = row + ny[i]
				# index를 벗어나면 건너뛰기
				if dx<0 or dx>=n or dy<0 or dy>=n:
					continue

				friend = desk[dy][dx]
				if friend in like:
					one_cnt +=1
					
			# 빈 자리라면 앉을 후보에 추가 함
			if desk[row][col] == 0:
				one[row,col] = one_cnt
			
	# 주변에 친구가 가장 많은 자리에 앉힌다
	one_max = max(one.values())
	# 주변 친구가 가장 많은 좌표들을 받을 배열(어러개 존재 할 시)
	one_list = []
	for key, value in one.items():
		if value == one_max:
			one_list.append(key)
			
	# 주변 친구가 가장 많은 것이 여러개 존재하지 않는다면
	# 그 자리에 앉힌다
	if len(one_list) == 1:
		desk[one_list[0][0]][one_list[0][1]] = stu
		
	# 여러개 존재한다면 > 2번조건
	# ----------------------2번 조건 -----------------------
	else :
		for idx in one_list:
			two_cnt = 0
			row = idx[0]
			col = idx[1]
			
			# 주변에 빈자리가 몇개 있는지 찾기
			for i in range(4):
				dx = col + nx[i]
				dy = row + ny[i]
				# index를 벗어나면 건너뛰기
				if dx<0 or dx>=n or dy<0 or dy>=n:
					continue
				
				blank = desk[dy][dx]
				if blank == 0:
					two_cnt +=1
			# two 딕셔너리에 빈칸 개수 저장
			if desk[row][col] == 0:
				two[row, col] = two_cnt
			
		# 주변에 빈자리가 가장 많은 자리에 앉힌다
		two_max = max(two.values())
		# 주변 빈자리가 가장 많은 좌표들을 받을 배열(어러개 존재 할 시 대비)
		two_list = []
		
		for key, value in two.items():
			if value == two_max:
				two_list.append(key)
		
		# 주변 빈자리가 가장 많은 것이 여러개 존재하지 않는다면
		# 그 자리에 앉힌다
		if len(two_list) == 1:
			desk[two_list[0][0]][two_list[0][1]] = stu
		
		# 아니라면? > 3번 조건
		# -----------3번 조건 -----------------------------------
		else:
			# 행과 열이 가장 작은 칸 > 그냥 row , col순으로 돌면서 빈자리 있으면 넣어주기
			#two_list = [(1,2), (2,3) ,(4,5)]
			for i in range(len(two_list)):
				row = two_list[i][0]
				col = two_list[i][1]
				if desk[row][col] == 0:
					desk[row][col] = stu
					break

# 만족도 구하기
solution = 0
for row in range(n):
	for col in range(n):
		
		cnt = 0
		stu = desk[row][col]
		like = student[stu]
		
		for i in range(4):
			dx = col + nx[i]
			dy = row + ny[i]
			# index를 벗어나면 건너뛰기
			if dx < 0 or dx >= n or dy < 0 or dy >= n:
				continue
			
			friend = desk[dy][dx]
			if friend in like:
				cnt += 1
	
		if cnt ==0:
			solution += 0
		elif cnt ==1 :
			solution +=1
		elif cnt ==2:
			solution+=10
		elif cnt ==3:
			solution+=100
		elif cnt ==4:
			solution += 1000

print(solution)
		
		
		