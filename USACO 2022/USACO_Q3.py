T = int(input())


def check(cases, var_num, indexes):
    output = set()
    for index in indexes:
        if cases[index][1] == '1':
            output.add(index)

    if output == indexes or output == set():
        return True

    for var in range(var_num):
        stuff = set()
        for index in indexes:
            if cases[index][0][var] == '1':
                stuff.add(index)
        if stuff != set() and stuff != indexes:
            anti_stuff = indexes.difference(stuff)
            anti_output = indexes.difference(output)
            if stuff.intersection(output) == stuff:
                return check(cases, var_num, anti_stuff)
            elif stuff.intersection(anti_output) == stuff:
                return check(cases, var_num, anti_stuff)
            elif anti_stuff.intersection(output) == anti_stuff:
                return check(cases, var_num, stuff)
            elif anti_stuff.intersection(anti_output) == anti_stuff:
                return check(cases, var_num, stuff)

    return False


for _ in range(T):
    input()
    N, M = [int(x) for x in input().split(' ')]
    cases = [input().split(' ') for __ in range(M)]

    if check(cases, N, set([x for x in range(M)])):
        print("OK")
    else:
        print("LIE")
