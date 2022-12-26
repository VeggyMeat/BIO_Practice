cards = [1, 2, 3, 4, 5, 6, 7, 8]


def break_shuffle(deck):
    new_deck = deck[1:]
    new_deck.extend([deck[0]])
    return new_deck


def out_riffle(deck):
    return [deck[0], deck[4], deck[1], deck[5], deck[2], deck[6], deck[3], deck[7]]


def in_riffle(deck):
    return [deck[4], deck[0], deck[5], deck[1], deck[6], deck[2], deck[7], deck[3]]


commands = input()


def follow_command(command, deck):
    count = 1
    bracket = 0
    record = ''
    for char in command:
        if not bracket:
            if char.isnumeric():
                count = int(char)
                
            elif char == 'i':
                for _ in range(count):
                    deck = in_riffle(deck)
                count = 1
                    
            elif char == 'o':
                for _ in range(count):
                    deck = out_riffle(deck)
                count = 1
                    
            elif char == 'b':
                for _ in range(count):
                    deck = break_shuffle(deck)
                count = 1

        else:
            record += char

        if char == '(':
            bracket += 1
        
        elif char == ')':
            bracket -= 1
            if not bracket:
                for _ in range(count):
                    deck = follow_command(record[:-1], deck)
                count = 1
                record = ''
    
    return deck


print(follow_command(commands, cards))