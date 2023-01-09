digits = int(input())
start = input()


def switch(num1, num2, word):
    small = min(num1, num2)
    large = max(num1, num2)
    return word[:small] + word[large] + word[small] + word[large + 1:]


bfs = [start, -1]
checked = set()
count = 0
while len(bfs) > 1:
    item = bfs.pop(0)
    if item == -1:
        count += 1
        bfs.append(-1)
    else:
        for x in range(digits - 1):
            small = min(int(item[x]), int(item[x + 1]))
            large = max(int(item[x]), int(item[x + 1]))
            add = False
            if x != 0:
                if small < int(item[x - 1]) < large:
                    add = True
            if x != digits - 2:
                if small < int(item[x + 2]) < large:
                    add = True

            if add:
                new = switch(x, x + 1, item)
                if new not in checked:
                    bfs.append(new)
                    checked.add(new)

print(count)
