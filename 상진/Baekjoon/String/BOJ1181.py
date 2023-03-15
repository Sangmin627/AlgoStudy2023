import sys
input = sys.stdin.readline

N = int(input())
words = list(set(input().rstrip() for _ in range(N)))
words.sort(key=lambda x : (len(x), x))

for word in words:
    print(word)