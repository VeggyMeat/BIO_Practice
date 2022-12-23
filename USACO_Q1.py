n_cows = int(input())
cows = input()
cows = cows.split(' ')
cows = [int(cow) for cow in cows]
cows.sort()

prev = cows[0]
total_num = n_cows
num = -1
best = 0
best_cost = 0

for cow in cows:
    if cow == prev:
        num += 1
    else:
        num += 1
        result = total_num * prev

        if result > best:
            best = result
            best_cost = prev
        elif result == best and best_cost > prev:
            best_cost = prev

        total_num -= num
        prev = cow
        num = 0

print(best, best_cost)
