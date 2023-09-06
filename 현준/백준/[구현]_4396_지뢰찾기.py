n= int(input())
arr = []
for i in range(2*n):
	arr.append(list(map(str,input())))

bomb = arr[:n]
play = arr[n:]
solution = [ ['.'for _ in range(n)] for _ in range(n)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [0,1,-1,-1,1,0,1,-1]

for x in range(n):
	for y in range(n):
		cnt = 0
		# 지뢰가 없는 곳을 찍은 경우
		if play[x][y] == 'x' and bomb[x][y] != '*':
			for i in range(len(dx)):
				nx = x+dx[i]
				ny = y+dy[i]
				if nx <0 or ny< 0 or nx >=n or ny>=n:
					continue
				if bomb[nx][ny] =='*':
					cnt +=1
			solution[x][y] = cnt
		# 지뢰가 있는 곳을 찍은 경우 > 모든 지뢰를 찍고 게임 종료
		elif play[x][y] == 'x' and bomb[x][y] == '*':
			for i in range(n):
				for j in range(n):
					if bomb[i][j] == '*':
						solution[i][j] = '*'


for i in range(n):
    for j in range(n):
        print(solution[i][j], end='')
    print()


