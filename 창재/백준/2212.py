N = int(input())
K = int(input())
sensor = sorted(list(set(map(int, input().split()))))
diff = []

print(sensor)

for i in range(len(sensor)-1):
    diff.append(sensor[i + 1] - sensor[i])

print(diff)
idx = []
for _ in range(K - 1):
    if not diff:
        break
    m = max(diff)
    diff.remove(m)

print(diff)
print(sum(diff))

# -2 3 / 6 7 8 / 10 / 12 14 15 / 18 20
#
# 0 2 0 2 2 1
# 1 1 2 1 2