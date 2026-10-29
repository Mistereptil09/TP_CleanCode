from Model import Card, CardRank


def check_score(cards : list[Card]) -> int:
    score: int = 0
    same_card: dict[CardRank, int] = {}
    for card in cards:
        same_card[card.rank] = same_card.get(card.rank, 0) + 1
        if card.rank.value > score:
            score = card.rank.value

    for value in same_card.values():
        if value >= 3:
            return 30
    return score
