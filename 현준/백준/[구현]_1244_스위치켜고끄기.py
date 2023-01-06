n = int(input())
status = list(map(int, input().split()))

student = int(input())

for _ in range(student):
	# 학생성별, 스위치 배열로 받기
	arr = list(map(int, input().split()))
	# 바꿀 스위치 변수 선언
	switch = arr[1]
	# 스위치 인덱스 = 스위치 -1
	switch_idx = arr[1] - 1
	# 만약 남자라면?
	if arr[0] == 1:
		for i in range(1, n + 1):
			# i = 1,2,3,4.....n
			# 배수라면 스위치 상태 변경
			if i % switch == 0:
				print(i)
				status[i - 1] = 1 - status[i - 1]
	
	# 만약 여자라면?
	else:
		# 대칭찾기
		
		# 스위치가 맨 끝에 있다면 > 대칭불가 바꾸고 종료
		print(switch_idx)
		if switch_idx == 0 or switch_idx == len(status) - 1:
			status[switch_idx] = 1 - status[switch_idx]
		# 아니라면 > 대칭체크
		else:
			# 스위치 기준 왼쪽, 오른쪽 배열 생성
			left = status[:switch_idx]
			right = status[switch_idx + 1:]
			
			# 대칭이므로 두 배열 기준 작은배열의 길이에 맞추기
			arr_len = min(len(left), len(right))
			left = left[:arr_len]
			right = right[:arr_len]
			# right 배열 뒤집기
			right.reverse()
			# 몇번째 까지 같아지는지 찾기
			check = -1
			for i in range(len(left) - 1, -1, -1):
				
				# i = 길이-1, 길이-2.....0
				if left[i] == right[i]:
					check = i
			# check == -1 인 경우 대칭이 아님 > 받은 스위치 변경
			if check == -1:
				status[switch_idx] = 1 - status[switch_idx]
			
			# 대칭이라면
			else:
				# 받은 스위치와 바꿀 스위치 까지 간격 생성
				interval = switch_idx - check
				# 스위치 위치 +- 간격의 스위치 상태 변경
				for idx in range(switch_idx - interval, switch_idx + interval + 1):
					status[idx] = 1 - status[idx]
					
num = len(status)//20
for i in range(1,num+2):
	print(*status[:20*i])



		