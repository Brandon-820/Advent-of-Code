# INPUT = "D7P1\example.txt"  # Output: 6440
INPUT = "D7P1\data.txt" # Output: 250946742

with open(INPUT, "r") as dataFile:
    data = dataFile.read()
    hands = []
    for line in data.splitlines():
        hand, bid = line.split()
        hands.append((hand, bid))


def camel_cards(hands):
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    hand_scores = []

    def hand_score(hand):
        counts = [hand.count(card) for card in '23456789TJQKA']
        if 5 in counts:
            score = 6  # Five of a kind
        elif 4 in counts:
            score = 5  # Four of a kind
        elif 3 in counts and 2 in counts:
            score = 4  # Full house
        elif 3 in counts:
            score = 3  # Three of a kind
        elif counts.count(2) == 2:
            score = 2  # Two pair
        elif 2 in counts:
            score = 1  # One pair
        else:
            score = 0  # High card
        return (score, [card_values[card] for card in hand])

    for hand, bid in hands:
        hand_scores.append((hand_score(hand), int(bid)))

    hand_scores.sort()

    total_winnings = sum(rank * bid for rank, (_, bid) in enumerate(hand_scores, 1)) # rank is the rank of the hand (1 is the highest rank) and bid is the bid for the hand  # enumerate(hand_scores, 1) is a list of tuples of the form (rank, (score, bid)) sorted by score in descending order

    return total_winnings

# hands = [('32T3K', '765'), ('T55J5', '684'), ('KK677', '28'), ('KTJJT', '220'), ('QQQJA', '483')]
print(camel_cards(hands))
