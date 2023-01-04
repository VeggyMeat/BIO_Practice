file = open("Day12.txt", 'r')
data = file.read()

grid = [list(x) for x in data.split('\n')]
adjacent = [(0, 1), (1, 0), (0, -1), (-1, 0)]
alph = 'abcdefghijklmnopqrstuvwxyz'

for y, row in enumerate(grid):
    for x, item in enumerate(row):
        if item == 'E':
            end = (x, y)
            grid[y][x] = 'z'
        elif item == 'S':
            start = (x, y)
            grid[y][x] = 'a'

max_x = len(grid[0])
max_y = len(grid)
bfs = [start, -1]
checked = set()
count = 0
while True:
    item = bfs.pop(0)
    if item == end:
        print(count)
        exit()
    elif item == -1:
        count += 1
        bfs.append(-1)
    else:
        for adj in adjacent:
            new = (item[0] + adj[0], item[1] + adj[1])
            if 0 <= new[0] < max_x and 0 <= new[1] < max_y:
                if new not in checked:
                    current = grid[item[1]][item[0]]
                    spot = grid[new[1]][new[0]]
                    if alph.index(current) + 1 >= alph.index(spot):
                        checked.add(new)
                        bfs.append(new)
