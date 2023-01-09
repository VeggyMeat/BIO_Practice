rule = input()
pass1 = input()
pass2 = input()
passwords = [pass1, pass2]

# take the rules and output valid combinations


def all_combos(ls):
    if len(ls) == 1:
        return ls[0]
    a = []
    for item in ls[0]:
        for rest in all_combos(ls[1:]):
            a.append(item + rest)
    return a


def valids(rule, length):
    combos = []
    bracket = False
    inside = ""
    prev = ""
    for symbol in rule:
        if not bracket and (symbol == 'x' or symbol == 'd' or symbol == 'u'):
            combos.append(symbol)
            prev = symbol
        elif symbol == '(':
            bracket = True
            inside = ""
        elif symbol == ')':
            bracket = False
        elif bracket:
            inside += symbol
        elif symbol == '*':
            if not inside:
                combos.pop()
            poss = []
            for x in range(13):
                if inside:
                    poss.append(inside * x)
                else:
                    poss.append(prev * x)
            inside = ""
            prev = ""
            combos.append(poss)
        elif symbol == '?':
            if not inside:
                combos.pop()
            if inside:
                combos.append(["", inside])
            else:
                combos.append(["", prev])
            inside = ""
            prev = ""

    possibilities = all_combos(combos)
    out = []

    for pos in possibilities:
        if len(pos) == length:
            out.append(pos)

    return out


for password in passwords:
    checks = valids(rule, len(password))
    valid = False
    for check in checks:
        failed = True
        for n, item in enumerate(check):
            if item == 'u':
                if int(password[n]) <= int(password[n - 1]):
                    failed = False
                    break
            elif item == 'd':
                if int(password[n]) >= int(password[n - 1]):
                    failed = False
                    break

        if failed:
            valid = True
            break

    if valid:
        print("Yes")
    else:
        print("No")
