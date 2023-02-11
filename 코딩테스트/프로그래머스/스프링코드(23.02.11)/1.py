lotteries = [[100, 100, 500], [1000, 1000, 100]]
answer = 0

# pos_lotteries = [0 for _ in range(len(lotteries))]
pos_lotteries = []
for lotter in lotteries:
    if lotter[0] >= lotter[1] + 1:
        pos_lotteries.append(1)
    else:
        pos_lotteries.append(lotter[0] / (lotter[1] + 1))

print(pos_lotteries)

max_value = max(pos_lotteries)
print(max_value)
if pos_lotteries.count(max_value) == 1:
    print(pos_lotteries.index(max_value) + 1)
else:
    max_gold = 0
    for idx, pos in enumerate(pos_lotteries):
        if pos == max_value and lotteries[idx][2] > max_gold:
            max_gold = lotteries[idx][2]
            answer = idx

print(answer + 1)