# almost complete

n_pebbles = int(input())
pebbles = [[int(x) for x in input().split()] for x in range(n_pebbles)]
o_banks = [int(x) for x in input().split()]
o_banks.sort()
if o_banks[0] > 0:
    banks = [-10000000, o_banks[0] - 0.5]
elif o_banks[1] < 0:
    banks = [o_banks[1] + 0.5, 10000000]
else:
    banks = [o_banks[0] + 0.5,  o_banks[1] - 0.5]
t = int(input())

out_distances = [t - x[2] for x in pebbles]
in_distances = [x - 2 for x in out_distances]
cords = [(x[0], x[1]) for x in pebbles]

points = [[], []]
for n, cord in enumerate(cords):
    distances = [out_distances[n], in_distances[n]]
    for t, distance in enumerate(distances):
        if cord[1] < -5:
            const = distance + cord[1]
        elif cord[1] > 5:
            const = distance - cord[1]
        else:
            for y in range(0, min(9, distance) + 1):
                if y != 0:
                    if y + cord[1] < 5:
                        left = distance - y
                        if y == distance:
                            points[t].append((cord[0], cord[1] + y))
                        else:
                            points[t].append((cord[0] + left, cord[1] + y))
                            points[t].append((cord[0] - left, cord[1] + y))

                    if cord[1] - y > -5:
                        left = distance - y
                        if y == distance:
                            points[t].append((cord[0], cord[1] - y))
                        else:
                            points[t].append((cord[0] + left, cord[1] - y))
                            points[t].append((cord[0] - left, cord[1] - y))
                else:
                    if y == distance:
                        points[t].append((cord[0], cord[1]))
                    else:
                        points[t].append((cord[0] + distance, cord[1]))
                        points[t].append((cord[0] - distance, cord[1]))
        if cord[1] < -5 < cord[1] + distance or cord[1] > 5 > cord[1] - distance:
            for y in range(-4, 5):
                left = const - y
                if left > 0:
                    points[t].append((cord[0] + left, y))
                    points[t].append((cord[0] - left, y))
                else:
                    points[t].append((cord[0], y))


def wrap_around(coasts, x):
    print(x)
    x = int((abs(x) % (2 * (abs(coasts[0]) + abs(coasts[1])))) * x / abs(x) + 1)
    print(x)
    if x > coasts[1]:
        between = x - coasts[1]
        x = int(coasts[1] - between)
    elif x < coasts[0]:
        between = x - coasts[0]
        x = int(coasts[0] - between)
    print(x)
    print('')
    return x


for state in range(2):
    points[state] = [(wrap_around(banks, cord[0]), cord[1]) for cord in points[state]]

print(points)

for x in range(-4, 5):
    for y in range(-4, 5):
        if y == o_banks[0] or y == o_banks[1]:
            print('X', end='')
        else:
            total = points[0].count((y, x)) - points[1].count((y, x))
            if total > 0:
                print('*', end='')
            elif total == 0:
                print('-', end='')
            else:
                print('o', end='')
    print('')
