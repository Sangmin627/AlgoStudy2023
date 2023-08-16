first = list(input())
second = list(input())

n = len(first)
m = len(second)

i = 0
j = 0
k = 0

answer = [[], []]

while i < n:
    if j == m:
        j = k
        i += 1
        continue

    if first[i] == second[j]:
        answer[0] += first[i]
        i += 1
        j += 1
        k = j
    else:
        j += 1

print(answer)

i = 0
j = 0
k = 0

while j < m:
    if i == n:
        i = k
        j += 1
        continue

    if first[i] == second[j]:
        answer[1] += first[i]
        i += 1
        j += 1
        k = i
    else:
        i += 1

print(answer)
print(max(len(answer[0]), len(answer[1])))