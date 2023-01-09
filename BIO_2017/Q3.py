parcels, max_weight, n_items, weight = map(int, input().split())

min_items = 1 + (weight - 1) // max_weight

bfs = [[]]
complete = set()
max_items = n_items - min_items * (parcels - 1)
while len(bfs) != 0:
    item = bfs.pop(0)
    length = len(item)
    items_left = max_items - length
    weight_left = weight - sum(item)
    if max_weight * items_left >= weight_left:
        if items_left > 1:
            for x in range(1, min(max_weight, weight_left) + 1):
                copy = item[:]
                copy.append(x)
                if x == weight_left:
                    copy.sort()
                    copy = tuple(copy)
                    if copy not in complete:
                        complete.add(copy)
                else:
                    copy.sort()
                    if copy not in bfs:
                        bfs.append(copy)

        elif items_left == 1:
            item.append(weight_left)
            item.sort()
            item = tuple(item)
            if item not in complete:
                complete.add(item)

items = {}
smallest = 999
largest = 0

for item in complete:
    if len(item) > largest:
        largest = len(item)
    if len(item) < smallest:
        smallest = len(item)

    if len(item) in items:
        items[len(item)] += 1
    else:
        items[len(item)] = 1


def perms(length, total, min_size, max_size):
    items = []

    if length * max_size < total or length * min_size > total:
        return

    if length == 1:
        return [[total]]

    for x in range(min_size, max_size + 1):
        temp = perms(length - 1, total - x, min_size, max_size)
        if temp:
            for item in temp:
                item.insert(0, x)
                items.append(item)

    return items


combos = perms(parcels, n_items, smallest, largest)
total = 0

if combos:
    for combo in combos:
        num = 1
        for item in combo:
            num *= items[item]
        total += num

    print(total)
else:
    print(0)
