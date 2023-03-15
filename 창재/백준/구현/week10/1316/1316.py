import sys

al = list('abcdefghijklmnopqrstuvwxyz')
dict = {}
for i in range(len(al)):
    dict[al[i]] = i

input = sys.stdin.readline
n = int(input())
answer = 0  # 정답 카운트

for k in range(n):

    ss = list(input().rstrip())
    flag = False
    memo = [0] * 26 # 알파벳 갯수 만큼

    i = 0
    while i < len(ss):
        cur = ss[i]

        if memo[dict[ss[i]]] != 0:  # 해당 알파벳 memo 값 조회
            flag = True
            break

        while i < len(ss) and ss[i] == cur:
            memo[dict[ss[i]]] += 1
            i += 1

    if flag:
        continue
    else:
        answer += 1

    print(k+1, "k번째 : ", memo)

print(answer)