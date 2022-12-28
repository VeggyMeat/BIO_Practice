cards = [int(x) for x in input().split()]

score = 0
for a, card1 in enumerate(cards):
    for b, card2 in enumerate(cards[a:]):
        if a == b:
            score += 1

for a, card1 in enumerate(cards):
    for b, card2 in enumerate(cards[a + 1:]):
        for c, card3 in enumerate(cards[a + b + 2:]):
            for d, card4 in enumerate(cards[a + b + c + 3:]):
                for e, card5 in enumerate(cards[a + b + c + d + 4:]):
                    if card1 + card2 + card3 + card4 + card5 == 15:
                        score += 1
                if card1 + card2 + card3 + card4 == 15:
                    score += 1
            if card1 + card2 + card3 == 15:
                score += 1
        if card1 + card2 == 15:
            score += 1

print(score)
