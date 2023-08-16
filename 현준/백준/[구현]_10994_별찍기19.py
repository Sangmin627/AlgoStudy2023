n = int(input())
# 1 > 1/ 2 > 5 / 3 > 9 / 4 > 13
# 길이 = 1 > 5 > 9 > 13  즉 4씩 증가 length = 1 + 4*(n-1) = 4n-3
# 정사각형 모양임 2차원 배열 생성하고 바깥에서 부터 채워간다
# 숫자가 커지면 큰 네모안에 이전의 네모가 반복되므로 재귀적으로 접근
length = 4*n -3
midle = int((length +1) /2)
star = [[' ' for _ in range(length)]for _ in range(length)]
# 가로 채우는 순서
# 0,length / 2 , length - 2 / 4 , length - 4
# 세로 채우는 순서
# 0,length / 2, length -2 .....

def draw(x,y):
	leng = 4*x -3
	if x == 1:
		star[midle-1][midle-1] = '*'
		return
	# 가로 테두리 채우기
	for i in range(y,y+leng):
		star[y][i] = '*'
		star[y+leng-1][i] = '*'
	#세로 테두리 채우기
	for i in range(y,y+leng):
		star[i][y] = '*'
		star[i][y+leng-1] = '*'
	
	return draw(x-1,y+2)

draw(n,0)

for i in range(length):
	for j in range(length):
		print(star[i][j], end = '')
	print()
	
	
	
	