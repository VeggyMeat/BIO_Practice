password = input()
valid = True
for length in range(1, 6):
    for x in range(len(password) + 1 - length):
        compare = password[x:length + x]
        if compare == password[length + x: 2 * length + x]:
            valid = False
            break
    if not valid:
        break

if valid:
    print("Accepted")
else:
    print("Rejected")
