grid = [[0 for _ in range(105)] for _ in range(105)]
start = 50
adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
p, s, n = [int(x) for x in input().split()]
p -= 1
gaps = [int(x) for x in input().split()]

for a in range(n):
    x = p % 5 + start
    y = p // 5 + start
    grid[y][x] += 1
    check = [(x, y)]
    while check:
        item = check.pop(0)
        if grid[item[1]][item[0]] >= 4:
            grid[item[1]][item[0]] -= 4
            for adj in adjacent:
                grid[item[1] + adj[1]][item[0] + adj[0]] += 1
                check.append((item[1] + adj[1], item[0] + adj[0]))

    p += gaps[a % s]
    p %= 25

for y in range(start, start + 5):
    for x in range(start, start + 5):
        print(grid[y][x], end='')
        if x != 54:
            print(' ', end='')
    print('')
