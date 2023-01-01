import math

num = int(input())

primes = [2, 3]
for x in range(4, num + 1):
    sqrt = math.sqrt(x)
    add = True
    for prime in primes:
        if prime > sqrt:
            break
        else:
            if x % prime == 0:
                add = False
    if add:
        primes.append(x)

count = 0
for prime in primes:
    if prime > num / 2:
        break
    if num - prime in primes:
        count += 1

print(count)
