a, b = input().split()

items = [a, b, a + b]

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_pat(item):
    if len(item) == 1:
        return True

    for x in range(1, len(item)):
        left = item[:x]
        right = item[x:]

        if alph.index(min(left)) > alph.index(max(right)):
            if is_pat(left[::-1]) and is_pat(right[::-1]):
                return True

    return False


for item in items:
    print(["NO", "YES"][is_pat(item)])
