import sys
sys.setrecursionlimit(10**6)

n=int(input())
tree=[0]*(n+1)

for i in range(n):
    x,y,z=map(int,input().split())
    tree[x]=[y,z]

print(tree)
visited =[0]*(n+1)

# dfs를 사용하면 이동거리계산은 어떻게?? 방문할 때 마다 카운트 하나씩 추가??
# 1번부터 시작함
# 돌아가는 경우는 어떻게 해야하지????????????????????????????????

cnt = 0
def dfs(n):
    visited[n] = 1
    global cnt
    cnt +=1
    for node in tree[n]:
        if visited[node] == 0: #and node != -1:
            dfs(node)

dfs(1)
print(cnt)
        
        
