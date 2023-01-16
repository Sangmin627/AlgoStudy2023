n = int(input())

tips = []
for _ in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)

answer = 0

for (idx,tip) in enumerate(tips):
    if tip - idx < 0:
        continue
    answer += (tip - idx)

print(answer)