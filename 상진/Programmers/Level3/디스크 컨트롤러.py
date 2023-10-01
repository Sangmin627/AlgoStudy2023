def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    answer = jobs[0][1]
    time = jobs[0][1] + jobs[0][0]
    size = len(jobs)

    jobs = sorted(jobs[1:], key=lambda x: x[1])
    while jobs:
        for i in range(len(jobs)):
            req, proc = jobs[i][0], jobs[i][1]
            if req <= time:
                time += proc
                answer += time - req
                jobs.pop(i)
                break
        else:
            time = jobs[0][0]

    return answer // size