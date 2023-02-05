H, W = map(int, input().split())

blocks = list(map(int, input().split()))

arr = [[0] * W for _ in range(H)]

for j in range(W):
    for i in range(blocks[j]):
        arr[i][j] = 1

answer = 0
for i in range(H):
    startIdx = -1
    endIdx = -1
    for j in range(W):
        if arr[i][j] == 1:
            endIdx = j
        if arr[i][j] == 0 and startIdx == -1 and endIdx != -1:
            startIdx = j
        if endIdx > startIdx and startIdx != -1:
            answer += endIdx - startIdx
            startIdx = -1

print(answer)