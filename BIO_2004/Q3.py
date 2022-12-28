morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

char_to_morse = {alphabet[x]: morse[x] for x in range(26)}

word = input()
code = ''.join([char_to_morse[x] for x in word])


def recursion(code, depth, chars):
    if len(code) == 0 and depth == chars:
        return 1

    if depth >= chars:
        return 0

    n = 0
    for thing in morse:
        if code.startswith(thing):
            n += recursion(code[len(thing):], depth + 1, chars)

    return n


print(recursion(code, 0, len(word)))
