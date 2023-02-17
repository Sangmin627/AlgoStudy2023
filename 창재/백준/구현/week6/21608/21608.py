import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    likes = [[] for _ in range(N*N + 1)]
    q_studentNumber = deque()

    for i in range(N*N):
        a = list(map(int, input().split()))
        q_studentNumber.append(a[0])
        likes[a[0]] = a[1:]
    print(q_studentNumber)
    print(likes)

    room = [[0] * N for _ in range(N)]
    print(room)

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while q_studentNumber:    # queue 에서 하나씩 꺼내 면서 입력된 학생 번호 부터 차례 대로
        studentNumber = q_studentNumber.popleft()
        print('queue : ', q_studentNumber)
        print('studentNumber : ', studentNumber)
        max_value = 0
        result_1 = [[0] * N for _ in range(N)]

        for x in range(N):  # 교실 한칸 한칸을 위해
            for y in range(N):
                if room[x][y] == 0:  # 빈 자리면
                    for i in range(4):  # 자리의 상하 좌우를 탐색 하기 위해
                        if 0 <= (x - dx[i]) < N and 0 <= (y - dy[i]) < N:  # 교실 크기를 벗어 나지 않는 선에서
                            if room[x - dx[i]][y - dy[i]] in likes[studentNumber]:  # 상하 좌우 값이 "좋아 하는 학생 번호" 중에 있다면
                                result_1[x][y] += 1    # +1 을 하라
                else:
                    result_1[x][y] = -1  # 아무 것도 없을 때(max_value = 0 일), 카운트 안되게 하기 위해

                max_value = max(max_value, result_1[x][y])

        print("result_1", result_1)
        print("max_value : ", max_value)
        print("room : ", room)
        # 모든 교실 다 돌면서 카운트 했다면 이제 가장 숫자가 큰 자리에 들어갈 거임.
        max_value_idx = []  # 최대값 인 곳의 좌표를 저장
        for x in range(N):
            for y in range(N):
                if result_1[x][y] == max_value:
                    max_value_idx.append((x, y))

        print("max_value_idx : ", max_value_idx)
        """
        1 단계
        """
        if len(max_value_idx) == 1:
            x, y = max_value_idx[0]
            room[x][y] = studentNumber
            print("1번 room : ", room)
            print()
            continue
        else:
            m_cnt = [0 for _ in range(len(max_value_idx))]
            for m in range(len(max_value_idx)):
                x, y = max_value_idx[m]
                for i in range(4):  # 자리의 상하좌우를 탐색하기 위해
                    if 0 <= (x - dx[i]) < N and 0 <= (y - dy[i]) < N:  # 교실 크기를 벗어나지 않는 선에서
                        if room[x - dx[i]][y - dy[i]] == 0: # 상하좌우에 0인값(빈칸)이 있으면
                            m_cnt[m] += 1  # +1 을 한다.

            print(m_cnt)
            m_cnt_max = max(m_cnt)
            if m_cnt.count(m_cnt_max) == 1:
                x, y = max_value_idx[m_cnt.index(m_cnt_max)]
                room[x][y] = studentNumber
                print("2번 room : ", room)
                print()
                continue

            # 2번까지 안되면,,,,
            else:
                result_3 = []
                for idx, m in enumerate(max_value_idx):
                    if m_cnt[idx] == m_cnt_max:
                        result_3.append(m)

                print("정렬 전 result_3 : ", result_3)
                result_3.sort() # 사실 정렬이 필요 없을지도,,
                print("정렬 후 result_3 : ", result_3)
                x, y = result_3[0]
                room[x][y] = studentNumber
                print("3번 room : ", room)
                print()
                continue

    print('최종 결과 : ', room)

    # 만족도 구하기
    satis = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            cnt = 0
            studentNumber = room[x][y]
            for i in range(4):
                if 0 <= (x - dx[i]) < N and 0 <= (y - dy[i]) < N:
                    if room[x - dx[i]][y - dy[i]] in likes[studentNumber]:
                        cnt += 1

            if cnt == 0:
                satis[x][y] = 0
            else:
                satis[x][y] = 10 ** (cnt - 1)

    print(satis)
    print(sum(map(sum, satis)))