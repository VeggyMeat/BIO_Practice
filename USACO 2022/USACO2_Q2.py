import math

T = int(input())

primes = [2]

for x in range(3, 100000):
    is_prime = True
    largest = math.sqrt(x)
    for prime in primes:
        if prime > largest:
            break
        if x % prime == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(x)
primes.insert(0, 1)


def count(x):
    prev = 1
    for prime in primes:
        if prime > x:
            return 1 + count(x - prev)
        elif prime == x:
            return 1
        prev = prime


print(count(7))
print(count(31285))

for x in range(T):
    N = int(input())
    a = [int(x) for x in input().split(' ')]
    winner = [(count(x)) % 2 == 0 for x in a]
    room = 0

    room += 1
    room %= N
