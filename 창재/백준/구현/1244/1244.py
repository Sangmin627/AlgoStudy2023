def switching(value): # 스위치 전체를 또 넘기는거보다 값만 넘기는게 메모리 낭비 안하고 좋은거 아님? 레퍼런스만 넘기는건가?
    if value == 1: return 0
    else: return 1

def decal(n, switch, number, i):
    if 0 <= (number - i) and (number + i) < n and switch[number - i] == switch[number + i]:  # 기준점 좌우
        switch[number - i], switch[number + i] = switching(switch[number - i]), switching(switch[number + i])
        i += 1
        decal(n, switch, number, i)
    else:
        switch[number] = switching(switch[number])
        # return switch # 여기다 쓰면 리턴값이 None이 됨. 왜?
    return switch

def men(n, switch, number):
    for idx in range(number-1, n, number):
        switch[idx] = switching(switch[idx])

    return switch

def women(n, switch, number):
    return decal(n, switch, number - 1, 1)


if __name__ == '__main__':
    n = int(input())
    switch = list(map(int, input().split(' ')))
    numberOfStudents = int(input())
    students = []
    for i in range(numberOfStudents):
        students.append(list(map(int, input().split(' '))))

    for idx, student in enumerate(students):
        if student[0] == 1:
            switch = men(n, switch, student[1])
        else:
            switch = women(n, switch, student[1])

    for idx, value in enumerate(switch):
        if idx != 0 and idx % 20 == 0:
            print()
        print(value, end=' ')