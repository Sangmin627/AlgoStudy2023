import sys

def dfs(network, v, visitied):
    # 방문 기록하기
    visitied[v] = True

    for i in network[v]:
        if not visitied[i]: # 방문 기록이 없으면
            dfs(network, i, visitied)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    link = int(input())

    # 네트워크 기록을 위한 2차원 리스트
    network = [[] for _ in range(N + 1)]

    # 방문 기록을 위한 리스트
    visitied = [False] * (N + 1)

    for i in range(link):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)    # 양방향 임으로.

    dfs(network, 1, visitied)

    # 시작점인 1을 제외한 나머지 count
    print(visitied.count(True) - 1)