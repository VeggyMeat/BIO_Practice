grid = [['.' for _ in range(11)] for _ in range(11)]

ant_1 = input().split(' ')
ant_2 = input().split(' ')

heading_to_tup = {"T": (0, -1), "R": (1, 0), "B": (0, 1), "L": (-1, 0)}
tup_to_heading = {(0, -1): "T", (1, 0): "R", (0, 1): "B", (-1, 0): "L"}

rotate_left = {(0, -1): (-1, 0), (1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1)}
rotate_right = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
headings = [heading_to_tup[ant_1[2]], heading_to_tup[ant_2[2]]]

coords = [(int(ant_1[0]), int(ant_1[1])), (int(ant_2[0]), int(ant_2[1]))]
coords[0] = (coords[0][0] - 1, 11 - coords[0][1])
coords[1] = (coords[1][0] - 1, 11 - coords[1][1])

ants = [True, True]

while True:
    num = input()
    if num.isnumeric():
        num = int(num)
        for turn in range(num):
            for ant in range(2):
                if ants[ant]:
                    coords[ant] = (coords[ant][0] + headings[ant][0], coords[ant][1] + headings[ant][1])
                    if coords[ant][0] < 0 or coords[ant][0] > 10 or coords[ant][1] < 0 or coords[ant][1] > 10:
                        ants[ant] = False
                        continue

                    if grid[coords[ant][1]][coords[ant][0]] == '.':
                        headings[ant] = rotate_right[headings[ant]]
                        grid[coords[ant][1]][coords[ant][0]] = '*'
                    else:
                        headings[ant] = rotate_left[headings[ant]]
                        grid[coords[ant][1]][coords[ant][0]] = '.'

        for row in grid:
            print(row)
        if ants[0]:
            print(coords[0][0] + 1, 11 - coords[0][1], tup_to_heading[headings[0]])
        else:
            print("Removed")
        if ants[1]:
            print(coords[1][0] + 1, 11 - coords[1][1], tup_to_heading[headings[1]])
        else:
            print("Removed")

    elif num == "-1":
        break
