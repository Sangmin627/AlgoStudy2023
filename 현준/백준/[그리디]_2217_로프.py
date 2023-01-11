n = int(input())
rope_list =[]
for i in range(n):
	rope_list.append(int(input()))

# 들수 있는 가장 큰 무게
# n빵 해서 나눠서 든다 큰놈 먼저? 작은놈 먼저?? > 상관없음 정렬해서 큰놈먼저하든 작은놈 먼저하든 하는게 중요한 것 같음
rope_list.sort(reverse = True)
solution_list = [-1]

for i in range(len(rope_list)):
	# 정렬 했으므로 rope_list[i]가 현재까지의 최솟값임, i+1은 로프의 개수임
	weight = rope_list[i]*(i+1)
	solution_list.append(weight)
	
print(max(solution_list))

