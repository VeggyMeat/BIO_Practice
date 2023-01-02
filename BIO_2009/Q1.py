words = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

word_in = input()


for n, word in enumerate(words):
    letters = word
    for letter in word_in:
        if letter == letters[0]:
            letters = letters[1:]

        if len(letters) == 0:
            print(n + 1)
            exit()

print("NO")
