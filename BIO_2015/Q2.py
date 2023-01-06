grid = [[0 for _ in range(10)] for _ in range(10)]
a, c, m = [int(x) for x in input().split()]
adjacent = [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
r = 0
# orient 1 up, orient 0 right


def place_valid(coords, length, orientation):
    start_coords = (coords[0], 9 - coords[1])
    for x in range(length):
        if orientation == 1:
            coords = (start_coords[0], start_coords[1] - x)
        else:
            coords = (start_coords[0] + x, start_coords[1] - x)

        if coords[0] > 9 or coords[0] < 0 or coords[1] > 9 or coords[1] < 0:
            return False

        if not valid_square(coords):
            return False
    return True


def valid_square(coords):

    for adj in adjacent:
        new = (adj[0] + coords[0], adj[1] + coords[1])
        if 0 <= new[0] < 10 and 0 <= new[1] < 10:
            if grid[new[1]][new[0]]:
                return False
    return True


def place_ship(coords, length, orientation):
    start_coords = (coords[0], 9 - coords[1])
    for x in range(length):
        if orientation == 1:
            grid[start_coords[1] - x][start_coords[0]] = 1
        else:
            grid[start_coords[1]][start_coords[0] + x] = 1


items = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
while items:
    r = a * r + c
    r %= m
    coords = (r % 10, (r // 10) % 10)
    r = a * r + c
    r %= m
    orient = r % 2
    if place_valid(coords, items[0], orient):
        place_ship(coords, items[0], orient)
        print(coords[0], coords[1], ["H", "V"][orient])
        items.pop(0)
