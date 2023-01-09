plan, p, q = input().split()
p = int(p)
q = int(q)

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

connections = []
chosen = ""

for x in range(len(plan)):
    item = plan[0]
    for letter in alph:
        if letter not in plan and letter not in chosen:
            chosen += letter
            connections.append((letter, item))
            connections.append((item, letter))
            break
    plan = plan[1:]

items = []
for item in alph:
    if item not in chosen:
        chosen += item
        items.append(item)

    if len(items) == 2:
        connections.append(tuple(items))
        connections.append((items[1], items[0]))
        break

rooms = {}

for letter in chosen:
    if letter not in rooms:
        rooms[letter] = []

    for connection in connections:
        if letter == connection[0]:
            rooms[letter].append(connection[1])

for letter in ''.join(sorted(chosen)):
    rooms[letter].sort()
    print(''.join(rooms[letter]))

room_counts = {letter: 0 for letter in chosen}
room_counts['A'] = 1

exit_counts = {connection: 0 for connection in connections}

place = "A"
out = ""

for x in range(1, q + 1):
    if room_counts[place] == 0:
        nextI = False
        for item in rooms[place]:
            if nextI:
                nextI = False
                exit_l = (place, item)
                exit_counts[exit_l] += 1
                exit_counts[exit_l] %= 2
                place = item
                break

            exit_l = (place, item)
            if exit_counts[exit_l] % 2 == 1:
                nextI = True

        if nextI:
            exit_p = rooms[place][-1]
            exit_l = (place, item)
            exit_counts[exit_l] += 1
            exit_counts[exit_l] %= 2
            place = exit_p

    else:
        exit_p = rooms[place][0]
        exit_l = (place, exit_p)
        exit_counts[exit_l] += 1
        exit_counts[exit_l] %= 2
        place = exit_p

    if x == p:
        out += place

    room_counts[place] += 1
    room_counts[place] %= 2

print(out + place)
