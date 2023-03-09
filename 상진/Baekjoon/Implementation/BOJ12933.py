s = list(input())
d = ['q','u','a','c','k']

ans = 0
flag = True
for i in range(len(s)):
    idx = 0
    if s[i] != 'q':
        continue
    for j in range(i,len(s)):
        if s[j] == '-':
            continue
        if s[j] == d[idx]:
            idx += 1
            s[j] = '-'
            if idx == 5:
                idx = 0
    ans += 1

    if idx != 0:
        flag = False
        break

if s.count('-') != len(s) or not flag:
    print(-1)
else:
    print(ans)
