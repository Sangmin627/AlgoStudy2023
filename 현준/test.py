left = [
	['q','w','e','r','t'],
	['a','s','d','f','g'],
	['z','x','c','v']
]

right = [
	['y','u','i','o','p'],
	['h','j','k','l'],
	['b','n','m']
]

def distance_left(x):
	for i in range(3):
		if x in left[i]:
			idx_tmp = left[i].index(x)
			idx_first=[i,idx_tmp]
			return idx_first
		
print(distance_left('w'))

test = 'test'
for i in test:
	print(i)
