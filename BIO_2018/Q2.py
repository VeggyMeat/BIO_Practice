n, word = input().split()
n = int(n)

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
wheel_one = alph

circle = list(alph)
wheel_two = ""

start = -1

for x in range(26):
    start += n
    start %= len(circle)
    wheel_two += circle.pop(start)
    start -= 1

print(wheel_two[:6])

out = ""
for letter in word:
    out += wheel_two[alph.index(letter)]
    wheel_two = wheel_two[1:] + wheel_two[0]

print(out)
