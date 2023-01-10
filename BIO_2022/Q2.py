r, b = map(int, input().split())
s, f = map(int, input().split())

hexagons = [x + 1 for x in range(25)]

adj = {0: [-6, -5, 1, 5, 4, -1], 1: [-5, -4, 1, 6, 5, -1]}
edges = {}

blue = 25
b_f = 6

red = 1
r_f = 1


def adjacent_hexagons(hex):
    row = (hex - 1) // 5
    column = (hex - 1) % 5
    mod = row % 2
    adjacents = []
    if column != 0:
        adjacents.append(hex - 1)
    else:
        adjacents.append(hex - 50)
    if column != 4:
        adjacents.append(hex + 1)
    else:
        adjacents.append(hex - 50)
    if mod == 0:
        if row != 0:
            adjacents.append(hex - 5)
            if column != 0:
                adjacents.append(hex - 6)
            else:
                adjacents.append(hex - 55)
        else:
            adjacents.append(hex - 100)
            adjacents.append(hex - 101)

        if row != 4:
            adjacents.append(hex + 5)
            if column != 0:
                adjacents.append(hex + 4)
            else:
                adjacents.append(hex - 45)
        else:
            adjacents.append(hex - 100)
            adjacents.append(hex - 101)

        adjacents = [adjacents[2], adjacents[1], adjacents[4], adjacents[5], adjacents[0], adjacents[3]]
    elif mod == 1:
        adjacents.append(hex - 5)
        adjacents.append(hex + 5)
        if column != 4:
            adjacents.append(hex - 4)
            adjacents.append(hex + 6)
        else:
            adjacents.append(hex - 55)
            adjacents.append(hex - 45)
        adjacents = [adjacents[4], adjacents[1], adjacents[5], adjacents[3], adjacents[0], adjacents[2]]

    return adjacents


def score():
    hexagon_scores = [[0, 0] for x in range(1, 26)]
    for edge in edges:
        for side in edge:
            if 0 < side < 26:
                if edges[edge] == "B":
                    hexagon_scores[side - 1][1] += 1
                elif edges[edge] == "R":
                    hexagon_scores[side - 1][0] += 1

    scores = [0, 0]
    for item in hexagon_scores:
        if item[0] > item[1]:
            scores[0] += 1
        elif item[1] > item[0]:
            scores[1] += 1

    return scores


for hex in range(1, 26):
    for item in adjacent_hexagons(hex):
        pair = (min(hex, item), max(hex, item))
        edges[pair] = 0

for _ in range(s):
    inbetween = adjacent_hexagons(red)[r_f - 1]
    pair = (min(inbetween, red), max(inbetween, red))
    edges[pair] = "R"

    r_f += 1
    if r_f > 6:
        r_f -= 6
    red += r
    if red > 25:
        red -= 25

    inbetween = adjacent_hexagons(blue)[b_f - 1]
    pair = (min(inbetween, blue), max(inbetween, blue))
    edges[pair] = "B"

    b_f -= 1
    if b_f < 1:
        b_f += 6
    blue += b
    if blue > 25:
        blue -= 25

sco = score()

for _ in range(f):
    most = (-1, 99, 0, 7, (-2, -2))

    for edge in edges:
        if not edges[edge]:
            edges[edge] = "R"
            new_sco = score()
            add = False

            if edge[0] > 0:
                direction = adjacent_hexagons(edge[0]).index(edge[1])
            else:
                direction = adjacent_hexagons(edge[1]).index(edge[0])
            if direction > 3:
                direction -= 3

            hex = min([x if x > 0 else 100 for x in edge])
            if new_sco[0] > most[0]:
                add = True
            elif new_sco[0] == most[0]:
                if new_sco[1] < most[1]:
                    add = True
                elif new_sco[1] == most[1]:
                    if hex < most[2]:
                        add = True
                    elif hex == most[2]:
                        if direction < most[3]:
                            add = True

            edges[edge] = 0
            if add:
                most = (new_sco[0], new_sco[1], hex, direction, edge)

    edges[most[4]] = "R"

    sco = score()

    most = (-1, 99, 26, 0, (-2, -2))

    for edge in edges:
        if not edges[edge]:
            edges[edge] = "B"
            new_sco = score()
            add = False

            if edge[0] > 0:
                direction = adjacent_hexagons(edge[0]).index(edge[1])
            else:
                direction = adjacent_hexagons(edge[1]).index(edge[0])
            if direction <= 3:
                direction += 3

            hex = max(edge)
            if new_sco[1] > most[0]:
                add = True
            elif new_sco[1] == most[0]:
                if new_sco[0] < most[1]:
                    add = True
                elif new_sco[0] == most[1]:
                    if hex > most[2]:
                        add = True
                    elif hex == most[2]:
                        if direction > most[3]:
                            add = True

            edges[edge] = 0
            if add:
                most = (new_sco[0], new_sco[1], hex, direction, edge)

    edges[most[4]] = "B"

    sco = score()

print(sco[0])
print(sco[1])
