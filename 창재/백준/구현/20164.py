import sys

def count_odd(N):
    count = 0
    for n in N:
        if int(n) % 2 == 1:
            count += 1

    return count

def dfs(listN, count):
    print()
    print("listN = ", listN)
    lenN = len(listN)
    print("lenN = ", lenN)

    if lenN == 1:
        answer.append(count)
        return
    elif lenN == 2:
        front = int(listN[0])
        back = int(listN[1])

        new = front + back
        c = count_odd(str(new))

        count += c
        dfs(str(new), count)
        count -= c
        return

    for i in range(1,lenN - 1): # 첫번째 구간
        for j in range(i + 1, lenN): # 두전빼 구간
            front = int(listN[:i])
            mid = int(listN[i:j])
            back = int(listN[j:])

            print("front = ", front)
            print("mid = ", mid)
            print("back = ", back)

            new = front + mid + back
            c = count_odd(str(new))
            count += c
            dfs(str(new), count)
            count -= c


input = sys.stdin.readline
N = input().strip()
answer = []

count = count_odd(N) # 초기값 세팅
dfs(N, count)

print(answer)
answer.sort()
print("min = ", answer[0])
print("max = ", answer[-1])

print(answer[0], answer[-1])