import math

n, m = [int(x) for x in input().split(' ')]


def recursion(number_ones, position):
    place = 1
    digits = number_ones
    inc = 0
    while place < position:
        inc = math.comb(digits, number_ones - 1)
        place += inc
        digits += 1

    place -= inc
    if number_ones == 1:
        return '1' + '0' * (digits - 1)
    else:
        out = recursion(number_ones - 1, position - place)
        return '1' + '0' * (digits - 1 - len(out)) + out


print(recursion(m, n))
