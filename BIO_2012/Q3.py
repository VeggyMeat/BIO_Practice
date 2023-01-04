chars = {0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}
outputs = []


def words_adj(word1, word2):
    dict1 = {}
    dict2 = {}
    for letter in word1:
        if letter in dict1:
            dict1[letter] += 1
        else:
            dict1[letter] = 1

    for letter in word2:
        if letter in dict2:
            dict2[letter] += 1
        else:
            dict2[letter] = 1

    dif = 0
    for letter in dict1:
        if letter in dict2:
            dif += abs(dict1[letter] - dict2[letter])
        else:
            dif += dict1[letter]

    for letter in dict2:
        if letter not in dict1:
            dif += dict2[letter]

    if dif <= 5:
        return True
    return False


all_words = {}
for x in range(1, 1000):
    word = ''.join([chars[int(y)] for y in str(x)])
    length = len(word)
    word = list(word)
    word.sort()
    word = ''.join(word)
    if length in all_words:
        if word not in all_words[length]:
            all_words[length].append(word)
    else:
        all_words[length] = [word]

for x in range(3):
    start_word, end_word = input().split()

    end_sorted = list(''.join([chars[int(y)] for y in end_word]))
    end_sorted.sort()
    end_sorted = ''.join(end_sorted)

    start = ''.join([chars[int(y)] for y in start_word])

    counter = 1
    checked = set()
    bfs = [start, -1]
    while end_sorted not in bfs:
        item = bfs.pop(0)
        if item == -1:
            counter += 1
            bfs.append(-1)
        else:
            length = len(item)
            for x in range(-5, 6):
                if length + x in all_words:
                    for thing in all_words[length + x]:
                        if words_adj(item, thing):
                            if thing not in checked:
                                bfs.append(thing)
                                checked.add(thing)

    print(counter)
