start = input()
dic = {"RG": "B", "RB": "G", "BG": "R", "GR": "B", "BR": "G", "GB": "R", "GG": "G", "RR": "R", "BB": "B"}


def recursion(letters):
    if len(letters) == 1:
        return letters[0]
    out = ""
    for x in range(len(letters) - 1):
        out += dic[letters[x] + letters[x + 1]]
    return recursion(out)


print(recursion(start))
