num = input()
print(''.join([{"pa": "1", "re": "2", "ci": "3", "vo": "4", "mu": "5", "xa": "6", "ze": "7", "bi": "8", "so": "9", "no": "0"}[num[x * 2: x * 2 + 2]] for x in range(len(num) // 2)]))