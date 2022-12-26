encrypted = input()
reversed_encrypted = encrypted[::-1]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
out = ''

for n, letter in enumerate(reversed_encrypted):
    if n != len(reversed_encrypted) - 1:
        num = alphabet.find(letter)
        num -= alphabet.find(reversed_encrypted[n + 1]) + 1
        num %= 26
        out += alphabet[num]
    else:
        out += letter

print(out[::-1])
