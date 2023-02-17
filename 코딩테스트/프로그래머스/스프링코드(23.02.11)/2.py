
grid = [".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]

answer = 0
new_grid = []
for i in range(len(grid)):
    new_grid.append(list(grid[i]))

for x in range(len(new_grid)):
    for y in range(len(new_grid[0])):
        if new_grid[x][y] == '#':
            answer += 1

print(answer)