dic = [0, 1, 2, 3, 4, 5, 5]
num = int(input())


def facts(a):
    l = a ** 0.5
    fact = []
    for b in range(2, a + 1):
        if b > l:
            break

        if a % b == 0:
            fact.append((b, a // b))

    return fact


for x in range(7, num + 1):
    factors = facts(x)
    if not factors:
        dic.append(dic[-1] + 1)
    else:
        dic.append(min(min([dic[pair[0]] + dic[pair[1]] for pair in factors]), dic[-1] + 1))

print(dic[-1])
