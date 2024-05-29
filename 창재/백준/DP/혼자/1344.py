import sys
import math

input = sys.stdin.readline
A = int(input()) * 0.01
B = int(input()) * 0.01
sosu = [2, 3, 5, 7, 11, 13, 17]

# PA = A 가 소수로 득점할 확률
# PB = B 가 소수로 득점할 확률
# P = PA + PB - (PA * PB)
PA = 0
PB = 0
for s in sosu:
    comb = math.comb(18, s)
    PA += comb * (A ** s) * ((1 - A) ** (18 - s))
    PB += comb * (B ** s) * ((1 - B) ** (18 - s))

P = PA + PB - (PA * PB)
print(P)