n = input()

odd = len(n) % 2 == 1

first_half = n[:len(n) // 2]

if odd:
    second_half = n[len(n) // 2 + 1:]
else:
    second_half = n[len(n) // 2:]

if odd:
    if int(first_half[::-1]) > int(second_half):
        print(first_half + n[len(n) // 2] + first_half[::-1])
    else:
        print(first_half + str(int(n[len(n) // 2]) + 1) + first_half[::-1])
else:
    if int(first_half[::-1]) > int(second_half):
        print(first_half + first_half[::-1])
    else:
        first_half = str(int(first_half) + 1)
        print(first_half + first_half[::-1])
