a = input()

out = ""
for x in range(2, 10):
    num = str(int(a) * x)
    anagram = True
    for y in range(10):
        if num.count(str(x)) != a.count(str(x)):
            anagram = False
            break

    if anagram:
        if out:
            out += " " + str(x)
        else:
            out += str(x)

print(out)
