import copy
import sys
sys.setrecursionlimit(10 ** 9)

def dfs(start, temp, dic, visited, answer, N):
    if len(temp) == N + 1:
        print("temp : ", temp)
        answer.append(copy.deepcopy(temp))
        print("visited = ", visited)
        return

    if start not in dic:
        return

    for k in dic[start]:
        if not visited[start][k]:
            visited[start][k] = True
            temp.append(k)
            dfs(k, temp, dic, visited, answer, N)

            if len(answer) >= 1:
                break

            visited[start][k] = False
            temp.pop()

    return


def solution(tickets):
    answer = []
    N = len(tickets)
    visited = {}
    dic = {}
    for t in tickets:
        if t[0] not in dic:
            visited[t[0]] = {}
            dic[t[0]] = []

        visited[t[0]][t[1]] = False
        dic[t[0]].append(t[1])

    for key in dic.keys():
        dic[key].sort()
    print(dic)
    print(visited)

    temp = ["ICN"]
    dfs("ICN", temp, dic, visited, answer, N)

    answer.sort()
    print("답 : ", answer)

    return answer[0]

tickets = [["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]
s = solution(tickets)
print(s)