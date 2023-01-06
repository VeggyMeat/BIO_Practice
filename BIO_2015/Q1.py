word_in = input()


def is_palindrome(word, first=True):
    count = not first
    half = len(word) // 2
    if len(word) % 2 == 1:
        word = word[:half] + word[half + 1:]

    for x in range(1, half + 1):
        if x == half:
            count += word[:half] == word[half:]
        elif word[:x] == word[len(word) - x:]:
            count += is_palindrome(word[x:len(word) - x], False)

    return count


print(is_palindrome(word_in))
