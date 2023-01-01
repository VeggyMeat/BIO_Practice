spot = input()
end = '1234567'


def op1(line):
    return line[1:4] + line[0] + line[4:]


def op2(line):
    return line[:3] + line[6] + line[3:6]


def op3(line):
    return line[3] + line[:3] + line[4:]


def op4(line):
    return line[:3] + line[4:] + line[3]


things = [op1, op2, op3, op4]

done = set()
bfs = [spot, -1]
count = 1
while end not in bfs:
    item = bfs.pop(0)
    if item == -1:
        count += 1
        bfs.append(-1)
    else:
        for func in things:
            new_line = func(item)
            if new_line not in bfs:
                if new_line not in done:
                    done.add(new_line)
                    bfs.append(new_line)

print(count)
