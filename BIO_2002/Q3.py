dic = [0, 1, 2, 3, 4, 5, 5]
num = int(input())


def facts(a):
    l = a ** 0.5
    for b in range(2, a + 1):
        if b > l:
            break

        if a % b == 0:
            return b, a // b

    return None, None


for x in range(7, num + 1):
    fact1, fact2 = facts(x)
    if fact1 is None:
        dic.append(dic[-1] + 1)
    else:
        value = dic[fact1] + dic[fact2]
        for y in range(1, 5):
            if dic[-y] + y < value:
                value = dic[-y] + y
        dic.append(value)

print(dic[-1])
