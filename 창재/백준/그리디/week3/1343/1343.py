# 덮을 수 없는 경우 예외 사용자 생성
class CanNotCover(Exception):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    inputBoard = list(input())

    count = 0
    recordBoard = []
    for idx, i in enumerate(inputBoard):
        if i == 'X':
            count += 1
            if idx == len(inputBoard) - 1:  # 마지막 인덱스 일 때,
                recordBoard.append(count)
        elif i == '.':   # . 이면
            if count != 0:
                recordBoard.append(count)
            recordBoard.append(i)
            count = 0

    result = []
    try:
        for i in recordBoard:
            if i == '.':        # '.' 이면 PASS
                result.append(i)
                continue
            elif i % 2 != 0:    # count 가 홀수면 예외 처리
                raise CanNotCover

            numberA = i // 4                    # AAAA 로 넢을 수 있는 횟수
            result.append('AAAA' * numberA)     # 그 만큼 추가
            numberB = (i - 4 * numberA) // 2    # BB 로 넢을 수 있는 횟수
            result.append('BB' * numberB)       # 그 만큼 추가

        print("".join(result))

    # CanNotCover 예외가 발생하면 -1 출력
    except(CanNotCover):
        print(-1)