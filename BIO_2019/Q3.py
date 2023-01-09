import copy

letters, start = input().split()
letters = int(letters)

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:letters]

alpha_set = set(list(alph))

bfs = [set(list(start))]
amount = [1]
count = 0

while len(bfs) > 0:
    item = bfs.pop(0)
    quantity = amount.pop(0)
    left = alpha_set.difference(item)

    if len(left) == 0:
        count += quantity
        continue

    for letter in left:
        num = alph.index(letter)
        if 1 <= num < letters - 1:
            if alph[num - 1] in item:
                if alph[num + 1] in left:
                    continue

        if 0 <= num < letters - 2:
            if alph[num + 1] in item:
                if alph[num + 2] in left:
                    continue

        if 1 < num:
            if alph[num - 1] in item:
                if alph[num - 2] in item:
                    continue

        new = copy.copy(item)
        new.add(letter)
        if new in bfs:
            amount[bfs.index(new)] += quantity
        else:
            bfs.append(new)
            amount.append(quantity)
