alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

n = int(input())

counter = 1
lengths = [[1 for x in range(36)]]
for x in range(35):
    items = []
    start = sum(lengths[-1])
    for item in lengths[-1]:
        start -= item
        if start > 0:
            items.append(start)
    lengths.append(items)

sums = []

total = 0
for item in lengths:
    total += sum(item)
    sums.append(total)

cumulative = []
total = 0
for item in lengths:
    line = []
    for thing in item:
        total += thing
        line.append(total)
    cumulative.append(line)

cumulative_in = []
for item in lengths:
    total = 0
    line = []
    for thing in item:
        total += thing
        line.append(total)
    cumulative_in.append(line)


def recursion(position):
    if position <= 36:
        return alph[position - 1]
    for n1, item1 in enumerate(sums):
        if item1 >= position:
            for a, item2 in enumerate(cumulative[n1]):
                if item2 >= position:
                    return alph[a] + recursion(position - cumulative_in[n1][a])


print(recursion(n))
