N, M = map(int, input().split())

C = [[0] * (i + 1) for i in range(N + 1)]

C[0][0] = 1
for n in range(1, N + 1):
    for m in range(n + 1):
        if m == 0 or n == m:
            C[n][m] = 1
            continue

        C[n][m] = C[n-1][m-1] + C[n-1][m]

# for c in C:
#     print(*c)

print(C[N][M])