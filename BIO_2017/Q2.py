#  incomplete

sides = {}

symbols = {0: "*", 1: "X", 2: "O"}


def adjacent_dots(dot, order):
    adjacent = []
    dot -= 1
    if dot // 6 != 0:
        adjacent.append(dot - 5)
    if order == 1:
        if dot % 6 != 5:
            adjacent.append(dot + 2)
    else:
        if dot % 6 != 0:
            adjacent.append(dot)
    if dot // 6 != 5:
        adjacent.append(dot + 7)
    if order == 2:
        if dot % 6 != 5:
            adjacent.append(dot + 2)
    else:
        if dot % 6 != 0:
            adjacent.append(dot)
    return adjacent


for dot1 in range(1, 37):
    for dot2 in adjacent_dots(dot1, 1):
        dots = [dot1, dot2]
        dots.sort()
        sides[tuple(dots)] = 0

squares = []

for y in range(5):
    for x in range(5):
        squares.append((y * 6 + x + 1, y * 6 + x + 7, y * 6 + x + 8, y * 6 + x + 2))


def get_score():
    score = [0, 0]
    for square in squares:
        pair = [square[0], square[1]]
        pair.sort()
        pair = tuple(pair)
        if sides[pair]:
            prev = square[-1]
            colour = sides[pair]
            add = True
            for dot in square:
                pair = [prev, dot]
                pair.sort()
                pair = tuple(pair)
                if sides[pair] != colour:
                    add = False
                    break
                prev = dot

            if add:
                score[colour - 1] +=1

    return tuple(score)


def print_board():
    for n, square in enumerate(squares):
        pair = [square[0], square[1]]
        pair.sort()
        pair = tuple(pair)
        if sides[pair]:
            prev = square[-1]
            colour = sides[pair]
            add = True
            for dot in square:
                pair = [prev, dot]
                pair.sort()
                pair = tuple(pair)
                if sides[pair] != colour:
                    add = False
                    break
                prev = dot

            if add:
                print(symbols[colour], end=' ')
            else:
                print(symbols[0], end=' ')
        else:
            print(symbols[0], end=' ')
        if n % 5 == 4:
            print('')


p1, m1, p2, m2, t = [int(x) for x in input().split()]

modifiers = [m1, m2]
positions = [p1, p2]

turns = 0
player = 0

score = (0, 0)

while turns != t:
    player += 1
    if player == 3:
        player = 1

    old_score = score
    score = (-1, -1)
    while old_score != score:
        positions[player - 1] += modifiers[player - 1]
        added = False
        while not added:
            if positions[player - 1] > 36:
                positions[player - 1] -= 36

            for dot in adjacent_dots(positions[player - 1], player):
                pair = (min(dot, positions[player - 1]), max(dot, positions[player - 1]))
                if not sides[pair]:
                    added = True
                    sides[pair] = player
                    break

            if not added:
                positions[player - 1] += 1

        score = get_score()

        turns += 1
        if turns == t:
            break

print_board()

print(score[0], score[1])