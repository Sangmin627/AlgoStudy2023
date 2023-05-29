def solution(fees, records):
    answer = []

    car_time = dict()  # 차 - 누적시간
    car_count = dict()  # 차 - In/Out (1이면 23:59 출차하기 위함)
    car_nums = set()  # 차량번호

    for r in records:
        tmp = r.split()
        car_num = tmp[1]
        car_nums.add(car_num)
        car_time[car_num] = []
        car_count[car_num] = 0

    for r in records:
        tmp = r.split()
        times = tmp[0].split(":")

        hours = times[0]
        minutes = times[1]
        time = int(hours) * 60 + int(minutes)

        car_num = tmp[1]
        op = tmp[2]

        if op == "IN":
            car_count[car_num] += 1
            car_time[car_num].append(time)
        else:
            car_count[car_num] -= 1
            car_time[car_num][-1] = time - car_time[car_num][-1]

    for car_num in car_nums:
        if car_count[car_num] == 1:
            time = 23 * 60 + 59
            car_time[car_num][-1] = time - car_time[car_num][-1]

    for car_num in car_nums:
        car_time[car_num] = sum(car_time[car_num])

    sorted_keys = sorted(car_time.keys())

    for key in sorted_keys:
        time = car_time[key]
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            time -= fees[0]
            if time % fees[2] == 0:
                mod = time // fees[2]
            else:
                mod = time // fees[2] + 1
            answer.append(fees[1] + mod * fees[3])

    return answer