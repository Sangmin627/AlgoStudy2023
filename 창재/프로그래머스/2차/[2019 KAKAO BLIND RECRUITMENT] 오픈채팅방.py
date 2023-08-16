def create_db(n_record):
    user_db = {}
    for n in n_record:
        if n[0] == 'Enter' or n[0] == 'Change':
            if n[1] not in user_db:
                user_db[n[1]] = n[2]
            else:
                user_db[n[1]] = n[2]

    return user_db


def print_result(n_record, user_db):
    answer = []
    for n in n_record:
        if n[0] == 'Enter':
            answer.append(user_db[n[1]] + "님이 들어왔습니다.")
        elif n[0] == 'Leave':
            answer.append(user_db[n[1]] + "님이 나갔습니다.")

    return answer


def solution(record):
    n_record = []
    for r in record:
        n_record.append(list(r.split()))
    print("n_record : ", n_record)

    # 사용자 DB 생성
    user_db = create_db(n_record)
    print("user_db : ", user_db)

    # 출력으로 바꾸기
    answer = print_result(n_record, user_db)
    print("answer : ", answer)

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)