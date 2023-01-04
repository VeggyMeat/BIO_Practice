n = int(input())

factors = []
t = 1
for x in range(2, n + 1):
    if n % x == 0:
        add = True
        for factor in factors:
            if x % factor == 0:
                add = False
                break

        if add:
            factors.append(x)
            t *= x

print(t)
