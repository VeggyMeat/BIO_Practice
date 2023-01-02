n_jugs, measure = [int(x) for x in input().split()]
jugs = [int(x) for x in input().split()]

bfs = [tuple([0 for _ in range(n_jugs)]), -1]
searched = set()
steps = 0
while True:
    item = bfs.pop(0)
    if item == -1:
        steps += 1
        bfs.append(-1)

    else:
        if measure in item:
            print(steps)
            break

        for n, jug in enumerate(item):
            if jug != jugs[n]:
                copy = list(item)
                copy[n] = jugs[n]
                copy = tuple(copy)
                if copy not in searched:
                    bfs.append(copy)
                    searched.add(copy)

            if jug != 0:
                copy = list(item)
                copy[n] = 0
                copy = tuple(copy)
                if copy not in searched:
                    bfs.append(copy)
                    searched.add(copy)

                for p, jug2 in enumerate(item):
                    if p != n:
                        if jug2 != jugs[p]:
                            copy = list(item)
                            poured = min(jug, jugs[p] - jug2)
                            copy[n] -= poured
                            copy[p] += poured
                            copy = tuple(copy)
                            if copy not in searched:
                                bfs.append(copy)
                                searched.add(copy)
