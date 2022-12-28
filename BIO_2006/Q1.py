word1 = input()
word2 = input()
dic1 = {}
dic2 = {}
for letter in word1:
    if letter in dic1:
        dic1[letter] += 1
    else:
        dic1[letter] = 1

for letter in word2:
    if letter in dic2:
        dic2[letter] += 1
    else:
        dic2[letter] = 1

if dic1 == dic2:
    print("Anagrams")
else:
    print("Not anagrams")
