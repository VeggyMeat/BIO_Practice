from functools import lru_cache

p, q, r = map(int, input().split())
n = int(input())

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


@lru_cache(maxsize=None)
def count(letters, length, repeats, max_first):
    total = 0
    if length == 1:
        total += letters
        if not max_first:
            total -= 1
        return total

    if max_first != 0:
        total += count(letters, length - 1, repeats, max_first - 1)
    total += (letters - 1) * count(letters, length - 1, repeats, repeats - 1)

    return total


def recursion(letters, length, repeats, counts, max_first, first_letter):
    total = 0

    if length == 1:
        for letter in alph[:letters]:
            if letter != first_letter or max_first != 0:
                total += 1

            if total == counts:
                return letter

    for letter in alph[:letters]:
        inc = 0
        if letter == first_letter:
            if max_first != 0:
                inc = count(letters, length - 1, repeats, max_first - 1)
                if total + inc >= counts:
                    return letter + recursion(letters, length - 1, repeats, counts - total, max_first - 1, first_letter)
        else:
            inc = count(letters, length - 1, repeats, repeats - 1)
            if total + inc >= counts:
                return letter + recursion(letters, length - 1, repeats, counts - total, repeats - 1, letter)

        total += inc


print(recursion(p, r, q, n, q, "Z"))
