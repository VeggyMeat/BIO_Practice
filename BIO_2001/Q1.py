friends = int(input())
friends = [x + 1 for x in range(friends)]
words = int(input())
start = -1

while len(friends) > 1:
    start += words
    start %= len(friends)
    friends.pop(start)
    start -= 1

print("Number " + str(friends[0]) + " is left")
