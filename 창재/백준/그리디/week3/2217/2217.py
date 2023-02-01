if __name__ == '__main__':
    n = int(input())

    rope = []
    for i in range(n):
        rope.append(int(input()))
    rope.sort()     # 가용 중량이 적은 로프순대로 계산하기 위해서 정렬

    # 초기값 설정
    min = rope[0]   # 가장 중량이 적은 로프
    max = min * n   # min로프 기준으로 계산한 최대 중량

    for idx, w in enumerate(rope):
        if w > min:
            min = w
            # 길이를 구하기 위해서 len(rope[idx:])로 했더니 "시간 초과" 뜸..
            # (n - idx) 로 바꿔 주니까 됐음..
            max_w = w * (n - idx)
            if max_w > max:
                max = max_w

    print(max)