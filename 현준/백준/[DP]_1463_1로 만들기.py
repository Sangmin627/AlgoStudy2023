n = int(input())

dp = [0]*(n+1)

for i in range(2,n+1):
	
	# 최악의 경우 > 1을 빼서 이전 숫자의 값을 맞춘다
	dp[i] = dp[i-1] + 1
	
	#2로 나누어 떨어지는 경우
	if i%2 == 0:
		dp[i] = min(dp[i], dp[int(i/2)]+1)
	
	if i%3 == 0:
		dp[i] = min(dp[i], dp[int(i/3)] + 1)

print(dp[n])

