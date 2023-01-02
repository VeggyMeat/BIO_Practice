grid = [[1 for x in range(11)] for y in range(11)]
die = (1, 6, 2, 5, 3, 4)
# UP DOWN TOP BOTTOM LEFT RIGHT

heading = 0
pos = (5, 5)

line1 = [int(x) for x in input().split()]
line2 = [int(x) for x in input().split()]
line3 = [int(x) for x in input().split()]

middle = [line1, line2, line3]

for n, line in enumerate(middle):
    for x, item in enumerate(line):
        grid[n + 4][x + 4] = item


def print_grid(pos):
    for y in range(pos[1] - 1, pos[1] + 2):
        if 0 <= y < 11:
            for x in range(pos[0] - 1, pos[0] + 2):
                if 0 <= x < 11:
                    print(grid[y][x], end='')
                else:
                    print('X', end='')

            print('')
        else:
            print('XXX')


while True:
    move = input()
    if move == '0':
        break
    elif move.isnumeric():
        move = int(move)
        if 0 < move < 101:
            for _ in range(move):
                grid[pos[1]][pos[0]] += die[0] - 1
                grid[pos[1]][pos[0]] %= 6
                grid[pos[1]][pos[0]] += 1

                if grid[pos[1]][pos[0]] == 2:
                    heading += 1
                    heading %= 4
                elif grid[pos[1]][pos[0]] == 3 or grid[pos[1]][pos[0]] == 4:
                    heading += 2
                    heading %= 4
                elif grid[pos[1]][pos[0]] == 5:
                    heading -= 1
                    heading %= 4

                # UP DOWN TOP BOTTOM LEFT RIGHT
                if heading == 0:
                    pos = (pos[0], pos[1] - 1)
                    die = (die[3], die[2], die[0], die[1], die[4], die[5])
                elif heading == 1:
                    pos = (pos[0] + 1, pos[1])
                    die = (die[4], die[5], die[2], die[3], die[1], die[0])
                elif heading == 2:
                    pos = (pos[0], pos[1] + 1)
                    die = (die[2], die[3], die[1], die[0], die[4], die[5])
                else:
                    pos = (pos[0] - 1, pos[1])
                    die = (die[5], die[4], die[2], die[3], die[0], die[1])

            print_grid(pos)
