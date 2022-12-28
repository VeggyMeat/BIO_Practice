import math

value = float(input())

top, bottom = int(value * 10000), 10000


def simplify_fraction(one, two):
    lowest = math.gcd(one, two)
    return one // lowest, two // lowest


top, bottom = simplify_fraction(top, bottom)

print(top, '/', bottom)
