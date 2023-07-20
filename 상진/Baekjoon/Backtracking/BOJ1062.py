import sys
input = sys.stdin.readline

N,K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
ans = -1

learned = ['a','n','t','i','c']
visited = [0] * 26

for i in range(26):
    if chr(i+97) in learned:
        visited[i] = 1

ans = -1
def back(idx):
    global ans
    if sum(visited) == K:
        cnt = 0
        for word in sliced:
            for w in word:
                idx = ord(w) - 97
                if not visited[idx]:
                    break
            else:
                cnt += 1
        ans = max(ans, cnt)
        return

    for i in range(idx,26):
        if not visited[i]:
            visited[i] = 1
            back(i+1)
            visited[i] = 0

if K < len(learned):
    print(0)
else:
    sliced = []
    for word in words:
        word = word[4:len(word)-4]
        tmp = ""
        for w in word:
            if w not in learned:
                tmp += w
        sliced.append(tmp)
    back(0)
    print(ans)