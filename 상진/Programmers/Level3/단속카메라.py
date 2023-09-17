def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    out = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > out:
            answer += 1
            out = routes[i][1]

    return answer