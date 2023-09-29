def solution(genres, plays):
    answer = []
    genres_dic = dict()
    plays_dic = dict()
    size = len(genres)

    for i in range(size):
        genre = genres[i]
        play = plays[i]
        if genre not in plays_dic.keys():
            plays_dic[genre] = [(play, i)]
        else:
            plays_dic[genre].append((play, i))

        if genres[i] not in genres_dic.keys():
            genres_dic[genre] = plays[i]
        else:
            genres_dic[genre] += plays[i]

    sorted_genres = sorted(genres_dic.items(), key=lambda x: -x[1])

    for key, val in sorted_genres:
        cnt = 0
        sorted_plays = sorted(plays_dic[key], key=lambda x: (-x[0], x[1]))
        for streaming_cnt, idx in sorted_plays:
            if cnt == 2:
                break
            answer.append(idx)
            cnt += 1

    return answer