import math

def solution(n, stations, w):
    def init_cover():
        covers = []
        for station in stations:
            start = station - w
            end = station + w
            if start < 1:
                start = 1
            if end > n:
                end = n
            covers.append([start, end])
        return covers

    def check_adjacent_cover(cover):
        start = covers[0][0]
        end = covers[0][1]

        for i in range(1, len(covers)):
            if start <= covers[i][0] <= end:
                covers[i][0] = end + 1
            start = covers[i][0]
            end = covers[i][1]

    def init_not_cover(covers):
        not_covers = []
        not_cover_start = 1
        not_cover_end = 1

        for cover in covers:
            not_cover_end = cover[0] - 1
            not_covers.append([not_cover_start, not_cover_end])
            not_cover_start = cover[1] + 1

        not_covers.append([not_cover_start, n])
        return not_covers

    def calculate_not_cover(not_covers):
        answer = 0
        for not_cover in not_covers:
            start = not_cover[0]
            end = not_cover[1]
            if start <= end:
                answer += math.ceil((end - start + 1) / (2 * w + 1))
        return answer

    covers = init_cover()
    check_adjacent_cover(covers)
    not_covers = init_not_cover(covers)
    return calculate_not_cover(not_covers)