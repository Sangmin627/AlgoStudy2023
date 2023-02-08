# 1개 오르기 or 2개 오르기
# 연속된 3개를 밟으면 안됨 > 1개 오르기 한번 했으면 그 다음은 무조건 2개 올라야함
# 마지막 계단은 무조건 밟아야함

stairs = [0]
n = int(input())
for _ in range(n):
	stairs.append(int(input()))

#  1, 2, 3, 4, 5, 6 이 있을때
# 6은 무조건 밟아야함 > 1) 5를 밟는 경우 or 2) 4를 밟는 경우에 따라서 나눠짐
# 1)의 경우 4를 밟을 수 없음
# 2)의 경우 5를 밟을 수 없음
# >>> n개의 계단이 있는 경우
# n-1번째의 계단을 밟는 경우 > n-2번째의 계단을 밟으면 안됨  > 1,2,3,......,n-3,n-2,n-1,n > dp[n] = dp[n-3] + n-1 + n
# n-2번째의 계단을 밟는 경우 > n-1번째의 계단을 밟으면 안됨  > 1,2,3,......,n-3,n-2,n-1,n > dp[n] = dp[n-2] + n

dp =[0]
for i in range(1,n+1):
	if i ==1 :
		dp.append(stairs[1])
	elif i ==2 :
		dp.append(stairs[1]+stairs[2])
	elif i ==3 :
		tmp = max( (stairs[1]+stairs[3]),(stairs[2]+stairs[3]))
		dp.append(tmp)
	else:
		tmp = max( (dp[i-3]+stairs[i-1]+stairs[i]) , dp[i-2]+stairs[i])
		dp.append(tmp)

print(dp[n])