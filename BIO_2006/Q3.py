score, drats = [int(x) for x in input().split()]

to_check = [0, -1]
next = []
amounts = [1, -1]
count = 0

while len(to_check) > 0 and count != drats:
    item = to_check.pop(0)
    quant = amounts.pop(0)
    if item == -1:
        count += 1
        amounts.append(-1)
        to_check.extend(next)
        to_check.append(-1)
        next = []
    else:
        if count == 0:
            double = 2
        else:
            double = 1
        for x in range(1, 21):
            if x * double + item <= score:
                if x * double + item not in next:
                    next.append(x * double + item)
                    amounts.append(quant)
                else:
                    amounts[next.index(x * double + item) + len(to_check)] += quant

if score in to_check:
    print(amounts[to_check.index(score)])
else:
    print(0)
