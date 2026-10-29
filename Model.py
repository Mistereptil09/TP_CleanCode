from enum import Enum, IntEnum


class CardRank (IntEnum):
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    valet = 11
    queen = 12
    king = 13
    As = 14

class CardSuit(Enum):
    Heart = 1
    Diamonds = 2
    Clubs = 3
    Spades = 4

class Card:
    def __init__(self, rank : CardRank, suit : CardSuit):
        self.rank = rank
        self.suit = suit