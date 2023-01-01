layout = input()
links = {0: [1, 2, 3, 4, 5, 6, 7, 8], 1: [0, 2, 8], 2: [0, 1, 3], 3: [0, 2, 4], 4: [0, 3, 5], 5: [0, 4, 6], 6: [0, 5, 7], 7: [0, 6, 8], 8: [0, 1, 7]}
previous_states = [layout]
player = 0
to_marker = {0: 'O', 1: 'X'}


def loss_check(board, piece):
    blank = board.index('E')
    for link in links[blank]:
        if board[link] == piece:
            if valid_move(board, link):
                return False
    return True


def valid_move(board, pos_from):
    if pos_from == 0:
        return True
    piece = board[pos_from]
    if board[links[pos_from][1]] == piece and board[links[pos_from][2]] == piece:
        return False
    return True


def play_move(board, pos_from):
    board = list(board)
    board[board.index('E')] = board[pos_from]
    board[pos_from] = 'E'
    return ''.join(board)


def play_turn(turn, board):
    blank = board.index('E')

    valid = []

    player_piece = to_marker[turn]
    for pos in links[blank]:
        if board[pos] == player_piece:
            if valid_move(board, pos):
                valid.append(pos)

    for pos in valid:
        new_layout = play_move(board, pos)
        if loss_check(new_layout, to_marker[(turn + 1) % 2]):
            return new_layout

    new_valid = []
    for pos in valid:
        losing = False
        new_layout = play_move(board, pos)
        new_blank = new_layout.index('E')
        for new_pos in links[new_blank]:
            if new_layout[new_pos] == to_marker[(turn + 1) % 2]:
                if valid_move(new_layout, new_pos):
                    losing = True
                    break
        if not losing:
            new_valid.append(pos)

    if new_valid:
        return play_move(board, new_valid[0])
    else:
        return play_move(board, valid[0])


while True:
    step = input()
    if step == 'n':
        layout = play_turn(player, layout)
        print(layout)
        previous_states.append(layout)

        player += 1
        player %= 2
        if loss_check(layout, to_marker[player]):
            player -= 1
            player %= 2
            print("Player", player + 1, "wins")
            break
    elif step == 'r':
        while True:
            layout = play_turn(player, layout)
            if layout in previous_states:
                print("Draw")
                break
            previous_states.append(layout)

            player += 1
            player %= 2
            if loss_check(layout, to_marker[player]):
                print(layout)
                player -= 1
                player %= 2
                print("Player", player + 1, "wins")
                break
        break
