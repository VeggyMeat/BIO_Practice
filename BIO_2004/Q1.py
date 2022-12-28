import datetime

baktuns, katuns, tuns, uinals, kins = map(int, input().split())

baktuns -= 13
katuns -= 20
tuns -= 7
uinals -= 16
kins -= 3

katuns += baktuns * 20
tuns += katuns * 20
uinals += tuns * 18
kins += uinals * 20

months = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

year = 2000
step = 366

while kins > step:
    if year % 4 == 0:
        step = 366
    else:
        step = 365
    kins -= step
    year += 1

month = 1

if year % 4 == 0:
    for n, _ in enumerate(months):
        if n != 0:
            months[n] += 1

for n, day in enumerate(months):
    if kins > day:
        month += 1
    elif n != 0:
        kins -= months[n - 1]
        break
    else:
        break

print(kins + 1, month, year)
