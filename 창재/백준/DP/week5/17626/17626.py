"""
- 재귀로 푸려니까 머리가 터질 거같음.
- 인덱스 1부터 차례로 채워 나가기로함.
- 점화식 : f(n) = r**2 + f(n - r**2)
- r 을 1 부터 1씩 증가 시키면서 f(n - r**2)  이 가장 작은 값을 찾음.
- 마지막 +1 해서 저장.
"""
import sys

n = int(sys.stdin.readline())

dp = [0, 1]

for i in range(2, n + 1):
    min_value = 4  # 4보다 크면 어차피 의미 없음.
    r = 1

    while r**2 <= i:
        min_value = min(min_value, dp[i - r**2])
        r += 1

    dp.append(min_value + 1)

print(dp[n])