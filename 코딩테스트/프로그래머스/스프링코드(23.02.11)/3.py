def pelindrom(arr):
    flag = True
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            flag = False
            break

    if flag:
        return True
    else:
        return False


def solution(queries):
    answer = []

    for init_arr in queries:
        print('init_arr', init_arr)
        turn = 0
        for i in range(len(init_arr)//2):
            if init_arr[i] > init_arr[-i-1]:
                while init_arr[i] != init_arr[-i-1]:
                    init_arr[i] -= 1
                    turn += 1

            elif init_arr[i] < init_arr[-i-1]:
                while init_arr[i] != init_arr[-i-1]:
                    init_arr[-i-1] -= 1
                    turn += 1
            print('2init_arr', init_arr)
        print('turn : ', turn)

        if turn%2 == 0:
            answer.append(0)
        else:
            answer.append(1)

    return answer


if __name__ == '__main__':
    arr = [[0, 2, 0, 1], [0, 1, 0, 1]]

    print(solution(arr))