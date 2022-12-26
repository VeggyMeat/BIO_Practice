word1 = list(input())
word2 = list(input())

alphabet1 = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
alphabet2 = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")

words1 = ""
words2 = ""

for letter in word1:
    if letter in alphabet1:
        alphabet1.remove(letter)
        words1 += letter

for letter in alphabet1:
    words1 += letter

for letter in word2:
    if letter in alphabet2:
        alphabet2.remove(letter)
        words2 += letter

for letter in alphabet2:
    words2 += letter

words2 = words2[::-1]

grid1 = [[words1[x * 5 + y] for y in range(5)] for x in range(5)]
grid2 = [[words2[x * 5 + y] for y in range(5)] for x in range(5)]

for x in range(5):
    print(' '.join(grid1[x]) + '    ' + ' '.join(grid2[x]))

letter = input()
while letter != 'Q':
    if letter == 'E':
        word_in = input()
        if len(word_in) % 2 == 1:
            word_in += 'X'

        word_out = ''

        for x in range(len(word_in) // 2):
            letter1 = word_in[x * 2]
            letter2 = word_in[x * 2 + 1]

            pos1 = words1.find(letter1)
            pos2 = words2.find(letter2)
            pos1 = (pos1 % 5, pos1 // 5)
            pos2 = (pos2 % 5, pos2 // 5)

            if pos1[1] == pos2[1]:
                word_out += grid1[pos1[1]][(pos1[0] + 1) % 5]
                word_out += grid2[pos2[1]][(pos2[0] + 1) % 5]
            else:
                word_out += grid1[pos2[1]][pos1[0]]
                word_out += grid2[pos1[1]][pos2[0]]

        print(word_out)

    elif letter == 'D':
        word_in = input()

        word_out = ''

        for x in range(len(word_in) // 2):
            letter1 = word_in[x * 2]
            letter2 = word_in[x * 2 + 1]

            pos1 = words1.find(letter1)
            pos2 = words2.find(letter2)
            pos1 = (pos1 % 5, pos1 // 5)
            pos2 = (pos2 % 5, pos2 // 5)

            if pos1[1] == pos2[1]:
                word_out += grid1[pos1[1]][(pos1[0] - 1) % 5]
                word_out += grid2[pos2[1]][(pos2[0] - 1) % 5]
            else:
                word_out += grid1[pos2[1]][pos1[0]]
                word_out += grid2[pos1[1]][pos2[0]]

        if word_out[-1] == 'X':
            word_out = word_out[:-1]

        print(word_out)
    letter = input()
