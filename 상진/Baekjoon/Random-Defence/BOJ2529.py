import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(str, input().split()))
idx = 0
ans = []
tmp = []

def dfs():
    global idx
    if len(tmp) == 0:
        for i in range(10):
            tmp.append(str(i))
            dfs()
            tmp.pop()
    if len(tmp) == N+1:
        ans.append("".join(tmp))
        return
    for i in range(10):
        if str(i) not in tmp:
            if arr[idx] == '<' and len(tmp) >= 1:
                if i > int(tmp[-1]):
                    tmp.append(str(i))
                    idx += 1
                    dfs()
                    tmp.pop()
                    idx -= 1
            elif arr[idx] == '>' and len(tmp) >= 1:
                if i < int(tmp[-1]):
                    tmp.append(str(i))
                    idx += 1
                    dfs()
                    tmp.pop()
                    idx -= 1

dfs()
print(ans[-1])
print(ans[0])