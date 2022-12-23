import sys

N = int(input())
bales = [int(x) for x in input().split(' ')]
total = sum(bales)
each = total // N
roads = [[int(x) for x in input().split(' ')] for _ in range(N - 1)]

connected = {x: [] for x in range(1, N + 1)}
start = 0
sys.setrecursionlimit(100000)
for road in roads:
    connected[road[0]].append(road[1])
    connected[road[1]].append(road[0])

for item in connected:
    if len(connected[item]) == 1:
        start = item
        break

commands = []


def push_dict(value, prev, amount, items, dic, n, root=False):
    if value == root:
        return amount

    net = items[value - 1] + amount - each
    spot = False
    if len(dic[value]) != 1 and len(dic[value]) != 2:
        for branch in dic[value]:
            if prev != branch:
                if not spot:
                    spot = branch
                else:
                    prev_local = value
                    current = branch
                    while True:
                        if len(dic[current]) == 1:
                            break
                        for item in dic[current]:
                            if item != prev_local:
                                prev_local = current
                                current = item
                                break
                    net += push_dict(current, False, 0, items, dic, n + 1, root=value)
    elif len(dic[value]) == 1:
        if dic[value][0] == prev:
            return net
        spot = dic[value][0]
    else:
        if dic[value][0] == prev:
            spot = dic[value][1]
        else:
            spot = dic[value][0]
    if net > 0:
        commands.append([value, spot, net])
    elif net < 0:
        commands.append([spot, value, -net])
    return push_dict(spot, value, net, items, dic, n + 1, root=root)


push_dict(start, False, 0, bales, connected, 0)

buffer = []
out = []
for command in commands:
    for command1 in buffer:
        frm = command1[0]
        too = command1[1]
        amount = command1[2]
        if bales[frm - 1] - amount >= 0:
            bales[frm - 1] -= amount
            bales[too - 1] += amount
            out.append(command1)
            buffer.remove(command1)

    frm = command[0]
    too = command[1]
    amount = command[2]
    if bales[frm - 1] - amount < 0:
        buffer.append(command)
    else:
        bales[frm - 1] -= amount
        bales[too - 1] += amount
        out.append(command)

while len(buffer) > 0:
    for command1 in buffer:
        frm = command1[0]
        too = command1[1]
        amount = command1[2]
        if bales[frm - 1] - amount >= 0:
            bales[frm - 1] -= amount
            bales[too - 1] += amount
            out.append(command1)
            buffer.remove(command1)
            break

print(len(out))
for command in out:
    print(" ".join([str(x) for x in command]))
