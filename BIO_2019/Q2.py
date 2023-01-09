trail_length, instructions, moves = input().split()
trail_length, moves = int(trail_length), int(moves)

trail = []
spot = (0, 0)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

direction = 0

for n in range(moves):
    instruction = instructions[n % len(instructions)]
    if instruction == "L":
        direction -= 1
        direction %= 4
    elif instruction == "R":
        direction += 1
        direction %= 4

    new_spot = (directions[direction][0] + spot[0], directions[direction][1] + spot[1])
    count = 0
    while new_spot in trail and count < 4:
        direction += 1
        direction %= 4
        new_spot = (directions[direction][0] + spot[0], directions[direction][1] + spot[1])
        count += 1

    if count == 4:
        exit()

    trail.append(spot)
    if len(trail) > trail_length:
        trail.pop(0)

    spot = new_spot

print(spot)
