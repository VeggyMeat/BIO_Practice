ISBN = list(input())

for x, char in enumerate(ISBN):
    if char.isnumeric():
        ISBN[x] = int(char)
    elif char == 'X':
        ISBN[x] = 10

print(ISBN)

total = 0
position = 0
for n, digit in enumerate(ISBN):
    if digit == '?':
        position = (10 - n)
    else:
        total += (10 - n) * digit

out = 0
while (total + out * position) % 11 != 0:
    out += 1

if out == 10:
    print('X')
else:
    print(out)