n = int(input())

edgeStar = 1 + (n-1) * 4
arr = [[" "] * edgeStar for _ in range(edgeStar)]

def draw(n, x, y):
    if n == 1:
        arr[x][y] = "*"
        return
    starCount = 1 + (n - 1) * 4

    for j in range(y, y + starCount):
        arr[x][j] = "*"
        arr[x + starCount-1][j] = "*"

    for i in range(x, x + starCount):
        arr[i][y] = "*"
        arr[i][y + starCount-1] = "*"

    draw(n-1, x+2, y+2)

draw(n,0,0)
for i in range(edgeStar):
    for j in range(edgeStar):
        print(arr[i][j], end ="")
    print()



