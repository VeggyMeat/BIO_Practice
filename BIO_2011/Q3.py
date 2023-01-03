n = int(input())

options = ["19", "28", "37", "46", "55", "64", "73", "82", "91"]
digits = []
total = 0
count = 0
while total < n:
    count += 1
    total += 9 ** (count // 2)
    digits.append(total)


def recursion(num):
    if num <= 9:
        return options[num - 1]
    elif num <= 18:
        return options[num - 10][0] + '5' + options[num - 10][1]
    counter = 0
    while True:
        if digits[counter] >= num:
            counter -= 1
            dif = num - digits[counter]
            thing = 9 ** ((counter) // 2)
            add = options[(dif // thing)]
            out = recursion((dif % thing) + digits[(counter - counter % 2 - 2)])
            if counter % 2 == 1:
                half = len(out) // 2
                out = out[:half] + '5' + out[half:]
            return add[0] + out + add[1]
        counter += 1


if n == 1:
    print("5")
else:
    print(recursion(n - 1))
