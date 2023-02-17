import sys

input = sys.stdin.readline
N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

# append 보다 이게 좀더 빠름.
diff = [0] * (N - 1)
for i in range(N-1):
    diff[i] = sensor[i + 1] - sensor[i]

print('dif : ', diff)
diff.sort(reverse=True)
print('dif : ', diff)

print(sum(diff[K - 1:]))