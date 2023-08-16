import sys
input = sys.stdin.readline

H = input().rstrip()
H = H[6:H.index("</main>")]

def parse_tags(H): # 태그 파싱
    tags = []
    start, end = 0,0
    for i in range(len(H)):
        if H[i] == '<':
            start = i
        elif H[i] == '>':
            end = i
            tags.append([start, end])
            start = 0
            end = 0
    return tags

def parse_p(H): # p 태그 내에서의 태그 파싱
    text = ''
    tags_in_p = parse_tags(H)
    for i in range(len(tags_in_p)-1):
        text += H[tags_in_p[i][1]+1:tags_in_p[i+1][0]]

    return text.strip()

def remove_blanks(text):
    while "  " in text:
        text = text.replace("  ", " ")
    return text

tags = parse_tags(H)

start_p = 0
end_p = 0
for s,e in tags:
    pos = H[s:e+1]
    if "<div title=" in pos:
        tmp = pos.split('"')
        title = tmp[1]
        print("title :", title)
    elif "<p>" in pos:
        start_p = s
    elif "</p>" in pos:
        end_p = e
        text = parse_p(H[start_p:end_p+1])
        text = remove_blanks(text)
        print(text)