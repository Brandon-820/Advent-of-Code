
def camel_cards(hands):
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    hand_scores = []

    def hand_score(hand):
        counts = [hand.count(card) for card in '23456789TJQKA']
        score = [5, 4, 3, 2, 1, 0].index(max(counts))
        cards = sorted([(count, card_values[card]) for card, count in zip('23456789TJQKA', counts) if count > 0], reverse=True)
        return (score, cards)

    for hand, bid in hands:
        hand_scores.append((hand_score(hand), int(bid)))

    hand_scores.sort(reverse=True)

    total_winnings = sum(rank * bid for rank, (_, bid) in enumerate(hand_scores, 1))

    return total_winnings

hands = [('32T3K', '765'), ('T55J5', '684'), ('KK677', '28'), ('KTJJT', '220'), ('QQQJA', '483')]
print(camel_cards(hands))  # Output: 6440
