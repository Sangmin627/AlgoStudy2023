import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N,M = map(int, input().split())
dic = dict()
for i in range(N+M):
    P,F,C = map(str, input().split())
    if P not in dic.keys():
        dic[P] = []
    dic[P].append([F,C])
    if C == '1':
        if F not in dic.keys():
            dic[F] = []

def search(key):
    global files
    if dic[key]:
        for values in dic[key]:
            val,op = values[0], values[1]
            if op == '1':
                search(val)
            else:
                files.append(val)

Q = int(input())
queries = [input().rstrip() for _ in range(Q)]

for q in queries:
    q = q.split("/")[-1]
    files = []
    search(q)
    print(len(set(files)), len(files))