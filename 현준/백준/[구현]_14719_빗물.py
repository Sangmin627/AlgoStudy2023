h,w = map(int,input().split())
# h = 높이 >> 행
# w = 넓이 >> 열
height = list(map(int,input().split()))

basket = [[0 for _ in range(w)] for _ in range(h)]

for col in range(w):
	for row in range(height[col]):
		basket[row][col] = 1
	
basket.reverse()



#넘치지 않는 경우 까지 해아함 > 양쪽 끝이 모두 1이면 무조건 채움
#  0,0,1,0,0,0,1,0 인 경우는??
# 각 행 별로 1이 있는 인덱스를 모두 찾아서 인접한 인덱스 끼리 뺀 다음 -1 하면 됨

solution = 0
for arr in basket:
	
	idx_list = []
	for i in range(len(arr)):
		if arr[i] == 1:
			idx_list.append(i)
	
	# 각 행에 1개만 있는 경우 어차피 물 못담음
	if len(idx_list) >=2:
		for k in range(1,len(idx_list)):
			tmp = idx_list[k] - idx_list[k-1] -1
			solution += tmp
print(solution)


