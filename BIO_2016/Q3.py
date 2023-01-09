# incomplete

import math

i, p, q = [int(x) for x in input().split()]

primes = set()
checked = set()

two_powers = []

for x in range(int(math.log2(i)) + 2):
    two_powers.append(2 ** x)

bfs = [p, -1]
counter = 0
while bfs and q not in bfs:
    item = bfs.pop(0)
    if item == -1:
        counter += 1
        bfs.append(-1)
    else:
        for sign in range(-1, 3, 2):
            for power in two_powers:
                num = item + power * sign
                if num in checked:
                    if num in primes:
                        pass
                else:
                    sqrt = math.sqrt(num)
                    add = True
                    for x in range(2, int(sqrt) + 2):
                        if num % x == 0:
                            add = False
                    checked.add(num)
                    if add:
                        primes.add(num)
                        prime = True
                    else:
                        prime = False
