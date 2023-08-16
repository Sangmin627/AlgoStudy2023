import math

# 시간을 분으로 바꿔서 계산하는 메소드
def cul_time(after, before):
    a = list(map(int, after.split(':')))
    b = list(map(int, before.split(':')))

    return ((a[0] - b[0]) * 60) + (a[1] - b[1])

# 요금 리스트로 바꿔주는 메소드
def cul_fees(answer, fees):
    new_answer = []
    for i in range(len(answer)):
        if answer[i] <= fees[0]:
            answer[i] = fees[1]
        else:
            answer[i] = fees[1] + (math.ceil((answer[i] - fees[0]) / fees[2]) * fees[3])

    return answer


def solution(fees, records):
    accumulate = {}
    nrecords = []
    for record in records:
        r = list(record.split())
        nrecords.append(r)
        if r[1] not in accumulate:
            accumulate[r[1]] = 0

    nrecords.sort(key=lambda x: x[1])

    print("nrecords : ", nrecords)
    print("초기 accumulate : ", accumulate)

    i = 0
    l = len(nrecords)
    while i < l:
        if i == l - 1:
            accumulate[nrecords[i][1]] += cul_time('23:59', nrecords[i][0])
            break

        if nrecords[i][1] == nrecords[i + 1][1]:
            accumulate[nrecords[i][1]] += cul_time(nrecords[i + 1][0], nrecords[i][0])
            i += 2

        elif nrecords[i][1] != nrecords[i + 1][1]:
            accumulate[nrecords[i][1]] += cul_time('23:59', nrecords[i][0])
            i += 1

    print("계산된 accumulate : ", accumulate)
    answer = []
    keys = sorted(accumulate)
    for k in keys:
        answer.append(accumulate[k])

    print("분 : ", answer)
    answer = cul_fees(answer, fees)
    print("요금 : ", answer)

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fees, records)