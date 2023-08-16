n = int(input())

for i in range(n):
	num = int(input())
	dp = [0,1,2,4]
	
	if num >3:
		for j in range(4,num+1):
			tmp = dp[j-1] + dp[j-2] + dp[j-3]
			dp.append(tmp)
	print(dp[num])