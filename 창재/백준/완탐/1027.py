
N = int(input())
arr = [0]
arr.extend(list(map(int, input().split())))
memo = [0 for _ in range(N + 1)]

for x1 in range(1, N + 1):
    for x2 in range(x1 + 1, N + 1):

        y1 = arr[x1]
        y2 = arr[x2]
        a = (y2 - y1) / (x2 - x1)
        b = y1 - (a * x1)

        def function(gradient, d, x):
            return (gradient * x) + d

        flag = True
        for i in range(x1 + 1, x2):
            y = function(a, b, i)

            if arr[i] >= y:
                flag = False
                break

        if flag:
            memo[x1] += 1
            memo[x2] += 1

print("memo = ", memo)
print(max(memo))