grid = [list(input()) for _ in range(4)]

drop_columns = [[grid[y][x] for y in range(4)][::-1] for x in range(4)]
column_start = [0, 0, 0, 0]

adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

score = 0


def block_search(checked, pos, board):
    checked.add(pos)
    letter = board[pos[0]][pos[1]]
    for add in adj:
        new = (pos[0] + add[0], pos[1] + add[1])
        if 0 <= new[0] < 4 and 0 <= new[1] < 4:
            if new not in checked and board[new[0]][new[1]] == letter:
                block_search(checked, new, board)


def find_blocks(board):
    blocks = []
    checked = set()
    for y in range(4):
        for x in range(4):
            cords = (y, x)
            if cords not in checked:
                check = set()
                block_search(check, cords, board)
                if len(check) > 1:
                    blocks.append(check)
                checked = checked.union(check)

    return blocks


def collapse_board(board):
    for x in range(4):
        last = []
        for y in range(3, -1, -1):
            if not board[y][x]:
                last.append(y)
            elif len(last) >= 1:
                spot = last.pop(0)
                board[spot][x] = board[y][x]
                board[y][x] = ''
                last.append(y)


while True:
    command = int(input())
    if command == 0:
        break
    else:
        for _ in range(command):
            blocks = find_blocks(grid)
            add_score = 1
            for block in blocks:
                add_score *= len(block)

            if add_score == 1:
                print("GAME OVER")
                print(score)
                exit()

            score += add_score

            for block in blocks:
                for item in block:
                    grid[item[0]][item[1]] = ''

            collapse_board(grid)

            for x in range(4):
                for y in range(3, -1, -1):
                    if not grid[y][x]:
                        grid[y][x] = drop_columns[x][column_start[x]]
                        column_start[x] += 1
                        column_start[x] %= 4

        for line in grid:
            print(''.join(line))

        print(score)
