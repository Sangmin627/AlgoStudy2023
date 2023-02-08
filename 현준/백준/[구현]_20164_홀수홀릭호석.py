num = str(input())

# 3개의 부분으로 나누는 방법???
# 12345 가 있을 떄 > 1_2_3_4_5 > 4개의 빈칸 중 2개에 들어가야함 > (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)
# 젤 처음에 잘라서 생기는 수의 경우 마다 각 경우가 파생이 됨
# ex) 123456789 > 12345,678,9 123,456,789 가 생겼을때 전자의 경우 12345 > 123,4,5 이런식으로
# 가지치기 하듯이 경우의 수가 생김 > 이 모든걸 계산해야 최댓값과 최솟값을 알아낼 수 있음
# 가치지기 형식으로 파생되므로 재귀함수를 이용해보자!!

solution_list = []

# cnt 를 어디서 초기화 해야하지? > 모든 경우의 수 마다 각각 다르게 기록이 되어야 하는데 ㅅㅂ;
# cnt 를 함수안에서 정의하면 함수가 호출 될 떄 마다 cnt 가 0으로 초기화 돠는데
# 처음 함수 호출 > 나누기 전의 홀수 개수 카운트 > 하위 함수의 출력값에 더하기 > 어떻게 하지??
# cnt를 함수의 매개변수로 추가하여 재귀함수가 호출 될 떄 마다 계속 더해준다 쎽쓰


def calculate(num,cnt):
	if len(num) >= 3:
		for idx in num:
			if int(idx)%2 != 0:
				cnt +=1
		
		# 2개로 쪼개어서 나누어지는 모든 경우의 수에 대해서 재귀함수를 돌려준다
		for first in range(1,len(num)-1):
			for last in range(first+1,len(num)):
				tmp = int(num[:first]) + int(num[first:last]) + int(num[last:])
				
				
				# 재귀함수 호출
				calculate(str(tmp),cnt)
	
	elif len(num)==2:
		
		for idx in num:
			if int(idx)%2 != 0:
				cnt +=1
		
		tmp = int(num[:1])+int(num[1:])
		
		#재귀함수 호출
		calculate(str(tmp),cnt)
	# 길이가 1 인 경우 종료
	else :
		if int(num) %2 != 0:
			cnt+=1
		solution_list.append(cnt)
		return

calculate(str(num),0)

print(min(solution_list), max(solution_list))
				
				
	
	

