left = [
	['q','w','e','r','t'],
	['a','s','d','f','g'],
	['z','x','c','v']
]

right = [
	[0,'y','u','i','o','p'],
	[0,'h','j','k','l'],
	['b','n','m']
]

def check(x):
	if (x in left[0]) or(x in left[1]) or (x in left[2]):
		return 'left'
	else :
		return 'right'

def distance_left(x,y):
	for i in range(3):
		if x in left[i]:
			idx_tmp = left[i].index(x)
			idx_first=[i,idx_tmp]
	for i in range(3):
		if y in left[i]:
			idx_tmp = left[i].index(y)
			idx_second=[i,idx_tmp]
	
	distance = abs(idx_first[0]-idx_second[0]) +abs(idx_first[1]-idx_second[1])
	return distance


def distance_right(x, y):
	
	for i in range(3):
		if x in right[i]:
			idx_tmp = right[i].index(x)
			idx_first = [i, idx_tmp]
			
	for i in range(3):
		if y in right[i]:
			idx_tmp = right[i].index(y)
			idx_second = [i, idx_tmp]
	
	distance = abs(idx_first[0] - idx_second[0]) + abs(idx_first[1] - idx_second[1])
	return distance
	

alpha_left , alpha_right = map(str,input().split())
target = str(input())

# 처음에 주어지는 것은 왼손검지, 오른손 검지의 첫번쪠 위치임
# 따라서 왼손이 움직이는 거리, 오른손 움직이는 거리를 각각 계산 하여 나중에 합하는게 편할듯
# 2차원 배열의 Index의 차이의 절대값으로 위치를 계산하자

#target 를 순회한다
result = 0
for i in target:
	# 왼쪽이면 처음 위치부 거리 계산하고, 손의 위치를 현재 위치로 초기화 시킨다
	if check(i) == 'left':
		result = result + distance_left(alpha_left,i)
		alpha_left = i
	# 오른쪽도 똑같이
	elif check(i) =='right':
		result = result + distance_right(alpha_right, i)
		alpha_right = i
		

# 이제까지 이동거리만 합했으므로 각 타자를 누르는 시간도 더해준다
#print(distance_left('o','b')) >> 이부분 주석처리 안했더니 출력에러가 아니라 그냥 틀렸다고 하더라
#망할 백준 ..
result = result + len(target)
print(result)



	


