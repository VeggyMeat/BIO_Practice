grid_size = int(input())

grid = [[int(x) for x in input().split()] for _ in range(grid_size)]

red = {1: (1, 3), 2: (0, 2), 3: (2, 3), 4: (0, 3), 5: (0, 1), 6: (1, 2)}
green = {1: (0, 2), 2: (1, 3), 3: (0, 1), 4: (1, 2), 5: (2, 3), 6: (0, 3)}

convert = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def search_lines(dic):
    score = 0
    checked = set()
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            coords = (x, y)
            if coords not in checked:
                loop = set()
                loop.add(coords)
                checked.add(coords)
                prev = coords
                connections = dic[item]
                connection = convert[connections[0]]
                spot = (x + connection[0], y + connection[1])
                while True:
                    if spot in loop:
                        score += len(loop)
                        break
                    elif spot in checked:
                        break
                    elif spot[0] < 0 or spot[0] >= grid_size or spot[1] < 0 or spot[1] >= grid_size:
                        break
                    spot_connections = dic[grid[spot[1]][spot[0]]]
                    coord_connections = [convert[x] for x in spot_connections]
                    places = [(spot[0] + x[0], spot[1] + x[1]) for x in coord_connections]
                    if prev not in places:
                        break
                    else:
                        index = (1 + places.index(prev)) % 2
                        loop.add(spot)
                        checked.add(spot)
                    prev = spot
                    spot = places[index]

    return score


print(search_lines(red), search_lines(green))
