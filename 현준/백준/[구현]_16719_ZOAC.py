word = str(input())

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
			'Q','R','S','T','U','V','W','X','Y','Z']


for _ in range(len(word)):
	num = 100
	for i in word:
		idx1 = alphabet.index(i)
		if idx1 <= num :
			num = idx1
	
	idx2 = word.index(alphabet[num])
	print(word[idx2])
	word = word[:idx2] + word[idx2+1:]