n,m,v = map(int,input().split())


graph = [[] for i in range(n+1)]

for i in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
	
visited=[0]*(n+1)

dfs_list = []
def dfs(v):
	visited[v] = 1
	dfs_list.append(v)
	for node in graph[v]:
		if visited[node] == 0:
			dfs(node)
dfs(v)
for i in dfs_list:
	print(i,end = " ")

print()
# bfs
from collections import deque
visited=[0]*(n+1)
bfs_list = []

def bfs(v):
	queue = deque()
	queue.append(v)
	visited[v] = 1
	bfs_list.append(v)
	while queue:
		v = queue.popleft()
		for i in range(1, n + 1):
			# 방문한적 없는 인접 노드 방문
			if visited[i] == 0 and  v in graph[i]:
				queue.append(i)
				visited[i] = 1
				bfs_list.append(i)

bfs(v)

for i in bfs_list:
	print(i,end = " ")
		
		
