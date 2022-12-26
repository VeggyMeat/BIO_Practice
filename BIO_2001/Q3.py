n_astronauts = int(input())
astronauts = [int(x) for x in input().split()]

searched = {}
best = 100000


def recursion(n, pack_here, left, there):
    global best
    if len(left) == 0:
        if best > n:
            best = n
        return n

    if n + sum(left) // 2 > best:
        return 99999

    results = []

    if pack_here:
        for x, person1 in enumerate(left):
            for y in range(x + 1, len(left)):
                person2 = left[y]
                new_left = left[:]
                new_left.remove(person1)
                new_left.remove(person2)
                new_left.sort()

                new_there = there[:]
                new_there.append(person1)
                new_there.append(person2)
                new_there.sort()
                key = (False, tuple(new_left), tuple(new_there))
                if key in searched:
                    amount = searched[key] + n + max(person1, person2)
                    results.append(amount)
                    if amount < best:
                        best = amount
                else:
                    results.append(recursion(n + max(person1, person2), False, new_left, new_there))
                    searched[key] = results[-1] - n - max(person1, person2)

    else:
        for person in there:
            new_left = left[:]
            new_left.append(person)
            new_left.sort()

            new_there = there[:]
            new_there.remove(person)
            new_there.sort()
            key = (True, tuple(new_left), tuple(new_there))
            if key in searched:
                amount = searched[key] + n + person
                results.append(amount)
                if amount < best:
                    best = amount
            else:
                results.append(recursion(n + person, True, new_left, new_there))
                searched[key] = results[-1] - n - person
        # smallest = min(there)
        # there.remove(smallest)
        # left.append(smallest)
        # return recursion(n + smallest, True, left, there)

    return min(results)


print(recursion(0, True, astronauts, []))
