states = int(input())

conditions = [input().split() for _ in range(states)]

dic = {}
state = 1
spot = 0
num = 0

tape = {x: 0 for x in range(-3, 4)}
map_dir = {'L': -1, 'R': 1}

for n, cond in enumerate(conditions):
    for x, cond1 in enumerate(cond):
        dic[(n + 1, x)] = [int(cond1[0]), map_dir[cond1[1]], int(cond1[2])]

iterations = int(input())

for _ in range(iterations):
    if spot not in tape:
        tape[spot] = 0
    command = dic[(state, tape[spot])]
    state = command[2]
    tape[spot] = command[0]
    spot += command[1]
    num += 1
    if state == 0:
        break

print(''.join([str(tape[x]) for x in range(-3, 4)]))
print(num)
