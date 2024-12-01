card_rankings = {'A': 0xC, 'K': 0xB, 'Q': 0xA, 'J': 0x9, 'T': 0x8, '9': 0x7, '8': 0x6,
                 '7': 0x5, '6': 0x4, '5': 0x3, '4': 0x2, '3': 0x1, '2': 0x0}

updated_card_rankings = {'A': 0xC, 'K': 0xB, 'Q': 0xA, 'T': 0x9, '9': 0x8, '8': 0x7, '7': 0x6,
                         '6': 0x5, '5': 0x4, '4': 0x3, '3': 0x2, '2': 0x1, 'J': 0x0}


def main():
    data = open('data/day7.txt', 'r')

    hand_bid_tuples = []
    # Parse data
    for line in data:
        hand, bid = line.split()
        hand_bid_tuples.append((hand, int(bid)))

    # Transform the hands into number representations for better sorting
    # Ranking into 7 groups, first group >= 6000000, 6000000 > second group >= 5000000, ...
    # Needs to be one million steps because the card ranking 0xCCCCC (AAAAA) has the value 838860
    # Further sort by card value, represent each char with a hex value, append them and parse them as a number and
    # add onto the group ranking value

    # Part 1
    # Transform hand into their respective value
    for index, (hand, bid) in enumerate(hand_bid_tuples):
        hand_ranking = calculate_hand_ranking(hand, False)
        hand_value = transform_hand_into_value(hand, False)
        hand_bid_tuples[index] = (hand_ranking + hand_value, bid)

    # Sort the hands ascending by the first value in the tuple
    hand_bid_tuples.sort(key=lambda x: x[0])

    result = 0
    # Calculate the entire value based on the bid and its ranking
    for index, (hand_value, bid) in enumerate(hand_bid_tuples):
        result += (index + 1) * bid

    print(result)

    # Part 2
    # Parse data again
    data = open('data/day7.txt', 'r')
    hand_bid_tuples = []
    for line in data:
        hand, bid = line.split()
        hand_bid_tuples.append((hand, int(bid)))

    for index, (hand, bid) in enumerate(hand_bid_tuples):
        hand_ranking = calculate_hand_ranking(hand, True)
        hand_value = transform_hand_into_value(hand, True)
        hand_bid_tuples[index] = (hand_ranking + hand_value, bid)

    # Sort the hands ascending by the first value in the tuple
    hand_bid_tuples.sort(key=lambda x: x[0])

    result = 0
    # Calculate the entire value based on the bid and its ranking
    for index, (hand_value, bid) in enumerate(hand_bid_tuples):
        result += (index + 1) * bid

    print(result)


def calculate_hand_ranking(hand, use_joker):
    # Represent cards as list of each card with its number of occurrences
    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    # A hand in poker is always improved by increasing the number of cards with the same type, so we can abuse this
    # fact to just add the amount of jokers to the card with the highest occurrence, be careful this only works if it's
    # not only jokers!
    if use_joker and 'J' in hand and hand != 'JJJJJ':
        joker_count = cards.pop('J')
        max_number_occurrence = max(cards, key=cards.get)
        cards[max_number_occurrence] += joker_count

    # Check for Five of a kind
    if len(cards) == 1:
        return 6_000_000
    # Check for Four of a kind
    elif any(count == 4 for (card, count) in cards.items()):
        return 5_000_000
    # Check for Full house
    elif any(count == 3 for (card, count) in cards.items()) and any(count == 2 for (card, count) in cards.items()):
        return 4_000_000
    # Check for Three of a kind
    elif any(count == 3 for (card, count) in cards.items()):
        return 3_000_000
    # Check for Two pair
    elif len([card for card in cards if cards[card] == 2]) == 2:
        return 2_000_000
    # Check for One pair
    elif any(count == 2 for (card, count) in cards.items()):
        return 1_000_000
    # Else, it's only a High card
    else:
        return 0


def transform_hand_into_value(hand, use_updated_rankings):
    value = 0
    for card in hand:
        value <<= 4
        value |= updated_card_rankings[card] if use_updated_rankings else card_rankings[card]
    return value


if __name__ == '__main__':
    main()
