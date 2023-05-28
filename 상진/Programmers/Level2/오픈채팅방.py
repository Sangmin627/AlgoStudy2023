def solution(record):
    answer = []
    id_name = dict()
    id_op = []

    for line in record:
        r = line.split()
        op = r[0]
        id = r[1]

        if op == "Leave":
            id_op.append([id, op])
        else:
            nickname = r[2]
            if op == "Enter":
                id_op.append([id, op])
            id_name[id] = nickname

    for i in id_op:
        name = id_name[i[0]]
        op = i[1]
        if op == "Enter":
            answer.append(name + "님이 들어왔습니다.")
        else:
            answer.append(name + "님이 나갔습니다.")

    return answer