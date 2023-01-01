rotors = [['A', 'D', 'B', 'C'], ['A', 'C', 'B', 'D']]
up_letter = {'A': 'D', 'D': 'C', 'C': 'B', 'B': 'A'}
letter_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
opp = {'A': 'D', 'B': 'C', 'C': 'B', 'D': 'A'}
letters = ['A', 'B', 'C', 'D']

place = int(input())
word = input()


def rotate_rotor(rotor):
    new_rotor = ['' for _ in range(4)]
    for n, value in enumerate(rotor):
        new_rotor[(n - 1) % 4] = up_letter[value]
    return new_rotor


first_rotate = place % 4
second_rotate = (place // 4) % 4

for _ in range(first_rotate):
    rotors[0] = rotate_rotor(rotors[0])

for _ in range(second_rotate):
    rotors[1] = rotate_rotor(rotors[1])

out = ""

for letter in word:
    letter1 = rotors[0][letter_num[letter]]
    letter2 = rotors[1][letter_num[letter1]]
    letter3 = opp[letter2]
    letter4 = letters[rotors[1].index(letter3)]
    letter5 = letters[rotors[0].index(letter4)]
    out += letter5

    first_rotate += 1
    first_rotate %= 4

    rotors[0] = rotate_rotor(rotors[0])
    if first_rotate == 0:
        second_rotate += 1
        second_rotate %= 4
        rotors[1] = rotate_rotor(rotors[1])

print(out)
