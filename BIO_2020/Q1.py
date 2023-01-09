numerals, n = input().split()
n = int(n)

numbers = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

for x in range(n):
    count = -1
    prev = False
    out = ""
    for letter in numerals:
        count += 1
        if prev and prev != letter:
            out += numbers[count - 1]
            out += prev
            count = 0
        prev = letter
    out += numbers[count]
    out += letter
    numerals = out

print(numerals.count("I"), numerals.count("V"))
