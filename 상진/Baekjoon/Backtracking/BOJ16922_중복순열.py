from itertools import combinations_with_replacement
N = int(input())
ans = set()

cr = list(combinations_with_replacement([1,5,10,50], N))
for c in cr:
    ans.add(sum(c))

print(len(ans))
