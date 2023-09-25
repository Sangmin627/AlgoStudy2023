import heapq

def solution(genres, plays):
    answer = []

    n = len(genres)  # 입력 갯수
    genres_dict = {}  # 장르 : [총합, [[i, plays], [i, plays], ...]]

    # 딕셔너리 초기화
    for i in range(n):
        g = genres[i]
        if g not in genres_dict:
            # g 장르의 딕셔너리 초기화
            genres_dict[g] = [plays[i], []]
            heapq.heappush(genres_dict[g][1], (-plays[i], i))
        else:
            genres_dict[g][0] += plays[i]
            heapq.heappush(genres_dict[g][1], (-plays[i], i))

    print(genres_dict)

    # 총 플레이수가 큰 장르 순으로 정렬
    genres_rank = list(genres_dict.keys())
    genres_rank.sort(key=lambda g: genres_dict[g][0], reverse=True)

    for genre in genres_rank:
        for _ in range(2):
            if genres_dict[genre][1]:
                result = heapq.heappop(genres_dict[genre][1])
                answer.append(result[1])

    print(answer)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [800, 600, 150, 800, 2500]
solution(genres, plays)