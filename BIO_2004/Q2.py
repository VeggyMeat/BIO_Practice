import copy

grid = [['-' for _ in range(7)] for _ in range(6)]

n = int(input())
setup_moves = map(int, input().split())


def drop_piece(column, piece, board):
    for y in range(5, -1, -1):
        if board[y][column] == '-':
            board[y][column] = piece
            return True
    return False


def print_board():
    for row in grid:
        print(''.join(row))


def check_win(piece, board):
    for row in board:
        streak = 0
        for item in row:
            if item == piece:
                streak += 1
                if streak == 4:
                    return True
            else:
                streak = 0

    for column in range(7):
        streak = 0
        for row in range(6):
            if board[row][column] == piece:
                streak += 1
                if streak == 4:
                    return True
            else:
                streak = 0

    for column in range(-2, 4):
        streak = 0
        for add in range(6):
            if 0 <= column + add < 7:
                if board[add][add + column] == piece:
                    streak += 1
                    if streak == 4:
                        print(column, add)
                        return True
                else:
                    streak = 0

    for column in range(3, 9):
        streak = 0
        for add in range(6):
            if 0 <= column - add < 7:
                if board[add][column - add] == piece:
                    streak += 1
                    if streak == 4:
                        print(column, add)
                        return True
                else:
                    streak = 0

    return False


def take_turn(player):
    for column in range(7):
        new_grid = copy.deepcopy(grid)
        drop_piece(column, pieces[player], new_grid)
        if check_win(pieces[player], new_grid):
            drop_piece(column, pieces[player], grid)
            return 'wins'
    
    for column in range(7):
        new_grid = copy.deepcopy(grid)
        drop_piece(column, pieces[(player + 1) % 2], new_grid)
        if check_win(pieces[(player + 1) % 2], new_grid):
            drop_piece(column, pieces[player], grid)
            return False

    for column in range(7):
        if grid[0][column] == '-':
            drop_piece(column, pieces[player], grid)
            return False

    return 'Draw'


player = 0
pieces = {0: '*', 1: 'o'}
for move in setup_moves:
    drop_piece(move - 1, pieces[player], grid)

    player += 1
    player %= 2

print_board()

while True:
    command = input()
    if command == 'n':
        result = take_turn(player)
        print_board()
        if result == 'Draw':
            print('Draw')
            break
        elif result == 'wins':
            print('Player', player + 1, 'wins')
            break
        player += 1
        player %= 2

    elif command == 'r':
        while True:
            result = take_turn(player)
            if result == 'Draw':
                print('Draw')
                break
            elif result == 'wins':
                print('Player', player + 1, 'wins')
                break
            player += 1
            player %= 2
        print_board()
        break
