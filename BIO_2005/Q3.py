actors = int(input())
scenes = [int(x) for x in input().split()]

to_do = [[0 for x in range(actors)]]
amount = [1]
perms = 0

while len(to_do) > 0:
    item = to_do.pop(0)
    quant = amount.pop(0)
    if item == scenes:
        perms += quant
    else:
        for n, thing in enumerate(item):
            copy = item[:]
            if n != 0:
                if thing < scenes[n] and item[n - 1] > thing:
                    copy[n] += 1
                    if copy in to_do:
                        amount[to_do.index(copy)] += quant
                    else:
                        to_do.append(copy)
                        amount.append(quant)
            else:
                if thing < scenes[n]:
                    copy[n] += 1
                    if copy in to_do:
                        amount[to_do.index(copy)] += quant
                    else:
                        to_do.append(copy)
                        amount.append(quant)

print(perms)
