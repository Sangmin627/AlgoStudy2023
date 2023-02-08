n = int(input())

# 자연수를 최소 갯수의 제곱수의 합으로 표현하기

# arr[n] = arr[n-1] + 1/ arr[n-4] +4 / arr[n-9] + 1/ arr[n-5] + 2 >> 5를 만드는데 필요한 개수
# >>> arr[n] = arr[n-x] + arr[x] > x를 어디까지 할 것인지가 중요
arr = [1]*(n+1)
from math import trunc
#limit = trunc(n**(0.5))

for i in range(1,n+1):
	cnt = 4
	limit = trunc(i ** (0.5))
	if limit == i**(0.5):
		arr[i] =1
	else :
		for j in range(1,limit+1):
			tmp = arr[i-j] + arr[j]
			if tmp < cnt:
				cnt = tmp
				arr[i] = cnt

print(arr[n])


