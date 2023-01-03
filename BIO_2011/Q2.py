nums = list("A23456789TJQK")
suits = ["C", "H", "S", "D"]

deck = [num + suit for suit in suits for num in nums]

shuffles = [int(x) for x in input().split()]

rows = []

while len(deck) > 0:
    for shuffle in shuffles:
        for x in range(shuffle - 1):
            if len(deck) < 1:
                break
            deck.append(deck.pop(0))
        if len(deck) < 1:
            break
        rows.append(deck.pop(0))

print(rows[0], rows[-1])


def valid_moves(cards):
    moves = []
    for x in range(len(cards) - 1, 0, -1):
        if cards[x] and cards[x - 1]:
            try:
                if cards[x][0] == cards[x - 1][0] or cards[x][1] == cards[x - 1][1]:
                    moves.append((x, x - 1))
            except IndexError:
                print(len(cards), cards)

        if x > 2:
            if cards[x][0] == cards[x - 3][0] or cards[x][1] == cards[x - 3][1]:
                moves.append((x, x - 1))

    return moves


def do_move(cards, amounts, move):
    cards[move[1]] = cards[move[0]]
    amounts[move[1]] += amounts[move[0]]
    cards.pop(move[0])
    num.pop(move[0])
    return cards, amounts


def output_info(cards):
    print(len(cards), cards[0])


game = rows[:]
num = [1 for _ in range(52)]

while len(game) > 1:
    possibles = valid_moves(game)
    if not possibles:
        break

    game, num = do_move(game, num, possibles[0])

output_info(game)

game = rows[:]
num = [1 for _ in range(52)]

while len(game) > 1:
    possibles = valid_moves(game)
    if not possibles:
        break

    largest = 0
    move = (0, 0)
    for possible in possibles:
        if num[possible[1]] + num[possible[0]] > largest:
            largest = num[possible[1]] + num[possible[0]]
            move = possible

    game, num = do_move(game, num, move)

output_info(game)

game = rows[:]
num = [1 for _ in range(52)]

while len(game) > 1:
    possibles = valid_moves(game)
    if not possibles:
        break

    largest = 0
    move = (0, 0)
    for possible in possibles:
        copy_game, copy_num = do_move(game[:], num[:], possible)

        num = len(valid_moves(copy_game))

        if num > largest:
            largest = num
            move = possible

    game, num = do_move(game, num, move)

output_info(game)
