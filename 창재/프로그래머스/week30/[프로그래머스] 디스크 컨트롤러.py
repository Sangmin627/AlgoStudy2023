import heapq


def solution(jobs):
    answer = 0
    N = len(jobs)
    # 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
    # 중복되는 애들이 있을 수 있으므로
    # jobs.sort(key = lambda x: x[0])
    jobs.sort()
    print(jobs)

    heap = []
    initJob = jobs.pop(0)
    heapq.heappush(heap, (initJob[1], initJob[0]))  # 작업 시간 먼저
    curTime = 0
    while heap:
        curJob = heapq.heappop(heap)
        print("curJob = ", curJob)

        if curTime >= curJob[1]:
            curTime += curJob[0]
        else:
            curTime = curJob[1] + curJob[0]  # 시작 시간 + 작업 시간

        answer += curTime - curJob[1]
        print("answer = ", answer)

        while jobs:
            if jobs[0][0] > curTime:
                if not heap:
                    possJob = jobs.pop(0)
                    heapq.heappush(heap, (possJob[1], possJob[0]))
                break

            possJob = jobs.pop(0)
            heapq.heappush(heap, (possJob[1], possJob[0]))

    a = int(answer / N)
    print(a)
    return a