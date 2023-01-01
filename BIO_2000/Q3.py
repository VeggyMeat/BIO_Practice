import random

sides = int(input())
dice1 = [int(x) for x in input().split()]
dice2 = [int(x) for x in input().split()]


def perms(l1, l2):
    dic = {}
    for x in l1:
        for y in l2:
            if x + y in dic:
                dic[x + y] += 1
            else:
                dic[x + y] = 1
    return dic


def dic_less(dic1, dic2):
    # dic2 reference, dic1 check
    for item in dic1:
        if item in dic2:
            if dic2[item] < dic1[item]:
                return False
        else:
            return False
    return True


off_by = min(dice1) + min(dice2)

dice1 = [x - min(dice1) for x in dice1]
dice2 = [x - min(dice2) for x in dice2]

biggest = max(dice1) + max(dice2)

combos = perms(dice1, dice2)

dice1.sort()
dice2.sort()

bfs = [[0]]
while len(bfs) > 0 and len(bfs[0]) < sides:
    item = bfs.pop(0)
    for x in range(item[-1], biggest + 1):
        copy = item[:]
        copy.append(x)
        bfs.append(copy)

bfs.remove(dice1)
if dice1 != dice2:
    bfs.remove(dice2)

random.shuffle(bfs)
found = False

for n, die1 in enumerate(bfs):
    search = [[0]]
    while len(search) > 0 and len(search[0]) < sides:
        item = search.pop(0)
        for x in range(item[-1], biggest + 1):
            copy = item[:]
            copy.append(x)
            if dic_less(perms(copy, die1), combos):
                search.append(copy)

    if search:
        die2 = search[0]
        die2 = [str(x + off_by - 1) for x in die2]
        die1 = [str(x + 1) for x in die1]
        print(' '.join(die1))
        print(' '.join(die2))
        found = True
        break

if not found:
    print("Impossible")
