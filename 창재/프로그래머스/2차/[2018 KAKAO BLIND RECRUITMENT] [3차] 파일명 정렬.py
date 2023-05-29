import re


def slice_files(files):
    slice_files = []
    for file in files:
        s = []
        d = re.search(r'\d+', file)

        s.append(file[:d.start()])
        s.append(file[d.start():d.end()])
        s.append(file[d.end():])

        slice_files.append(s)

    return slice_files


def solution(files):
    answer = []

    # HEAD, NUMBER, TAIL 컷
    files = slice_files(files)
    print(files)

    # 정렬
    files.sort(key=lambda f : ( f[0].casefold(), int(f[1]) ) )
    print(files)

    # 다시 합침
    for f in files:
        answer.append(''.join(f))
    print(answer)

    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
solution(files)