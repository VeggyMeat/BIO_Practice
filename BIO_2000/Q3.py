# incomplete

sides = int(input())

die_one = input().split(' ')
die_one = [int(x) for x in die_one]
die_one.sort()

die_two = input().split(' ')
die_two = [int(x) for x in die_two]
die_two.sort()


def calc_output(one, two):
    out = {}
    for num1 in one:
        for num2 in two:
            if num1 + num2 in out:
                out[num1 + num2] += 1
            else:
                out[num1 + num2] = 1
    return out


outputs = calc_output(die_one, die_two)


def all_die(sides, smallest, largest, first_largest=999):
    if sides == 1:
        out = []
        for x in range(smallest, largest + 1):
            out.append([x])
        return out
    dice = []
    for x in range(smallest, min(largest, first_largest) + 1):
        out = all_die(sides - 1, x, largest)
        for die in out:
            die.insert(0, x)
            dice.append(die)
    return dice


largest = die_one[-1] + die_two[-1] - 1
smallest = 1
first_largest = die_one[0] + die_two[0] - 1
possibles = all_die(sides - 1, smallest, largest, first_largest=first_largest)
found = []
print(len(possibles))

for x, die1 in enumerate(possibles):
    matching = []
    combinations = {}
    for n in range(sides):
        pass


print(found)
