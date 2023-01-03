letter1, letter2, n = input().split()
n = int(n)

alph_to_num = {"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[n - 1]: n for n in range(1, 27)}
num_to_alph = {n: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[n - 1] for n in range(1, 27)}

letter1 = alph_to_num[letter1]
letter2 = alph_to_num[letter2]

for _ in range(n - 2):
    new = letter1 + letter2
    new -= 1
    new %= 26
    new += 1
    letter1 = letter2
    letter2 = new

print(num_to_alph[letter2])
