n = int(input())
arr = list(map(int,input().split()))

# 맨 앞에 있는 사람일 수록 합에서 중복이 되므로
# 시간이 적게 걸리는 사람을 앞으로 보내야 함
arr.sort()
time = 0
for i in range(1,len(arr)+1) :
	tmp = sum(arr[:i])
	time += tmp
print(time)
	