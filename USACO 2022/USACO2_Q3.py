N = int(input())
stuff = [[int(x) for x in input().split(' ')] for _ in range(N)]


def condition(max_term, min_term, items, diag, n):
    dif = diag[0]
    cond1 = max(max_term, items[-1] + dif) - min(min_term, items[-1] + dif)
    cond2 = max(max_term, items[-1] - dif) - min(min_term, items[-1] - dif)
    if cond1 == cond2:
        if n + 1 < len(diag):
            return condition(max(max_term, items[-n-2]), min(min_term, items[-n-2]), items, diag, n + 1)
        else:
            return items[-1] + dif
    else:
        if cond1 == diag[n]:
            return items[-1] + dif
        elif cond2 == diag[n]:
            return items[-1] - dif
        else:
            raise ValueError


items = [0]

diagonals = [[] for x in range(N - 1)]
for x, item in enumerate(stuff):
    for y, num in enumerate(item[1:]):
        diagonals[x + y].append(num)

diagonals = [diagonal[::-1] for diagonal in diagonals]

for x in range(N - 1):
    if x == 0:
        items.append(items[0] + diagonals[0][0])
    else:
        if diagonals[x][0] == 0:
            items.append(items[-1])
        else:
            items.append(condition(items[-1], items[-1], items, diagonals[x], 0))

lowest = min(items)
print(" ".join([str(x - lowest) for x in items]))
