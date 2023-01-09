# stolen from Adavya

from functools import lru_cache

N, word = input().split()
N = int(N)

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in word:
    if alph[alph.index(letter) + 1] in word:
        if alph[alph.index(letter) + 2] not in word:
            print(0)
            exit()


# LRU cache remembers inputs to the function, and if same inputs are called, doesn't re-run, just gives back the same result at the previous one
@lru_cache(maxsize=None)
def num_blockchains(lets_left, earliest_let):
    if lets_left == 0:
        return 1

    sm = 0

    for letter in range(0, lets_left):
        if letter < earliest_let:
            sm += num_blockchains(lets_left - 1, letter)
        else:
            if letter == lets_left - 1:
                sm += num_blockchains(lets_left - 1, earliest_let)

    return sm


print(num_blockchains(N - len(word), alph.index(min(word))))
