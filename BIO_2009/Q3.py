num, pos = [int(x) for x in input().split()]

ways_to_make = {1: 1, 2: 2, 3: 4}

for x in range(4, num + 1):
    T_sum = 0
    for y in range(-1, -10, -1):
        if x + y > 0:
            T_sum += ways_to_make[x + y]
        else:
            break

    if x < 10:
        T_sum += 1
    ways_to_make[x] = T_sum


def recursion(n, place):
    total = 0
    for a in range(-1, max(-10, -n), -1):
        total += ways_to_make[n + a]
        if total >= place:
            total -= ways_to_make[n + a]
            return str(-a) + ' ' + recursion(n + a, place - total)

    return str(n)


print(recursion(num, pos))
