switchCount = int(input())
switch = [0] + list(map(int, input().split()))

studentCount = int(input())
student = [list(map(int, input().split())) for _ in range(studentCount)]

def flip(switchNumber):
    if switch[switchNumber] == 0:
        switch[switchNumber] = 1
    else:
        switch[switchNumber] = 0

def switchMan(switchNumber):
    for i in range(1, switchCount+1):
        if i % switchNumber == 0:
            flip(i)

def switchWoman(switchNumber):
    flip(switchNumber)
    switchLeft = switch[1:switchNumber]
    switchRight = switch[switchNumber+1:]
    switchLeft.reverse()

    count = min(len(switchLeft), len(switchRight))
    #좌우 대칭 계산
    for i in range(1,count+1):
        if switchLeft[i-1] == switchRight[i-1]:
            flip(switchNumber-i)
            flip(switchNumber+i)
        else:
            break

for (sex, switchNumber) in (student):
    if sex == 1:
        switchMan(switchNumber)
    else:
        switchWoman(switchNumber)

for i in range(1, switchCount+1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()