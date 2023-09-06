n=int(input())
v=int(input())
graph = [[] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(v):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번 컴퓨터부터 걸림
def dfs(node):
    visited[node] = 1
    for n in graph[node]:
        if visited[n] == 0 : #방문하지 않았다면?
            dfs(n) # 그 노드부터 bfs실행

# 1번 노드부터 dfs실행
dfs(1)

print(sum(visited)-1)
