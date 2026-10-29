from Model import Card, CardRank


def check_score(cards : list[Card]) -> int:
    if is_color(cards):
        return 45

    if is_straight(cards):
        return 40

    if is_brelan(cards):
        return 30

    score: int = 0
    for card in cards:
        if card.rank.value > score:
            score = card.rank.value
    return score

def is_straight(cards: list[Card]) -> bool:
    ranks = sorted(card.rank for card in cards)
    if len(set(ranks)) != len(ranks):
        return False

    lowest = ranks[0]
    highest = ranks[-1]
    if highest - lowest == 4:
        return True
    return False

def is_brelan(cards: list[Card]) -> bool:
    counts: dict[CardRank, int] = {}
    for card in cards:
        counts[card.rank] = counts.get(card.rank, 0) + 1

    for count in counts.values():
        if count == 3:
            return True
    return False

def is_color(cards: list[Card]) -> bool:
    color = cards[0].suit.value
    for card in cards:
        if card.suit.value != color:
            return False
    return True