start = input()
steps = int(input())
pos = int(input())

rules = {'A': 'B', 'B': 'AB', 'C': 'CD', 'D': 'DE', 'E': 'EE'}

power_two = [2 ** x for x in range(30)]
fib = [1, 1]
for x in range(30):
    fib.append(fib[-1] + fib[-2])

rules_inc = {'A': fib[:], 'B': fib[1:], 'C': power_two, 'D': power_two, 'E': power_two}


def recursion(letters, num, depth, max_depth):
    total = 0
    nxt = ''
    for n, letter in enumerate(letters):
        total += rules_inc[letter][max_depth - depth]
        if total >= num:
            nxt = letter
            total -= rules_inc[letter][max_depth - depth]
            break

    if depth == max_depth:
        return nxt
    else:
        return recursion(rules[nxt], num - total, depth + 1, max_depth)


print(recursion(start, pos, 0, steps))
