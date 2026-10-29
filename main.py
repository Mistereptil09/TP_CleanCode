from Model import Card, CardSuit


def check_score(cards : list[Card]) -> int:
    score: int = 0
    for card in cards:
        if card.rank.value > score:
            score = card.rank.value
    return score
