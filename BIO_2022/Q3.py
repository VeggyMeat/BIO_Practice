order, n = input().split(' ')
n = int(n)
order = list(order)

letters = order[:]
letters.sort()

spots = ['' for x in letters]
preferences = []

for letter in letters:
    position = order.index(letter)
    able = [letters[position]]
    for x in range(position - 1, -1, -1):
        if spots[x]:
            able.append(letters[x])
    spots[position] = letter
    able.sort()
    preferences.append(able)

number = 1
for spot in preferences:
    number *= len(spot)

out = ""
count = 1
for preference in preferences:
    number //= len(preference)
    if len(preference) == 1:
        out += preference[0]
    else:
        for letter in preference:
            if count + number > n:
                break
            count += number
        out += letter

print(out.upper())
