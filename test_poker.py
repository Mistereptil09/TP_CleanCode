import pytest

from Model import Card, CardRank, CardSuit
from main import check_score


class TestPoker:

    @pytest.mark.parametrize('hand', [[
        Card(CardRank.four, CardSuit.Diamonds),
        Card(CardRank.five, CardSuit.Spades),
        Card(CardRank.three, CardSuit.Heart),
        Card(CardRank.two, CardSuit.Clubs),
        Card(CardRank.nine, CardSuit.Diamonds),
    ]])
    def test_high_card(self, hand):
        assert(check_score(hand) == CardRank.nine.value)

    @pytest.mark.parametrize('hand', [
        [
            Card(CardRank.two, CardSuit.Diamonds),
            Card(CardRank.two, CardSuit.Clubs),
            Card(CardRank.two, CardSuit.Heart),
            Card(CardRank.five, CardSuit.Spades),
            Card(CardRank.nine, CardSuit.Diamonds),
        ],
        [
            Card(CardRank.king, CardSuit.Spades),
            Card(CardRank.king, CardSuit.Diamonds),
            Card(CardRank.king, CardSuit.Heart),
            Card(CardRank.three, CardSuit.Spades),
            Card(CardRank.seven, CardSuit.Diamonds),
        ],
    ])
    def test_brelan(self, hand):
        assert (check_score(hand) == 30)

    @pytest.mark.parametrize('hand', [
        [
            Card(CardRank.two, CardSuit.Diamonds),
            Card(CardRank.three, CardSuit.Spades),
            Card(CardRank.four, CardSuit.Heart),
            Card(CardRank.five, CardSuit.Clubs),
            Card(CardRank.six, CardSuit.Diamonds),
        ],
        [
            Card(CardRank.ten, CardSuit.Diamonds),
            Card(CardRank.valet, CardSuit.Spades),
            Card(CardRank.queen, CardSuit.Clubs),
            Card(CardRank.king, CardSuit.Heart),
            Card(CardRank.As, CardSuit.Diamonds),
        ]
    ])
    def test_suite(self, hand):
        assert (check_score(hand) == 40)

    @pytest.mark.parametrize('hand', [
        [
            Card(CardRank.two, CardSuit.Diamonds),
            Card(CardRank.three, CardSuit.Diamonds),
            Card(CardRank.two, CardSuit.Diamonds),
            Card(CardRank.five, CardSuit.Diamonds),
            Card(CardRank.six, CardSuit.Diamonds),
        ],
        [
            Card(CardRank.ten, CardSuit.Diamonds),
            Card(CardRank.valet, CardSuit.Diamonds),
            Card(CardRank.two, CardSuit.Diamonds),
            Card(CardRank.king, CardSuit.Diamonds),
            Card(CardRank.As, CardSuit.Diamonds),
        ]
    ])
    def test_suite(self, hand):
        assert (check_score(hand) == 45)

    @pytest.mark.parametrize('hand', [
        [
            Card(CardRank.two, CardSuit.Diamonds),
            Card(CardRank.two, CardSuit.Clubs),
            Card(CardRank.two, CardSuit.Heart),
            Card(CardRank.three, CardSuit.Spades),
            Card(CardRank.three, CardSuit.Diamonds),
        ],
        [
            Card(CardRank.king, CardSuit.Spades),
            Card(CardRank.king, CardSuit.Diamonds),
            Card(CardRank.king, CardSuit.Heart),
            Card(CardRank.four, CardSuit.Spades),
            Card(CardRank.four, CardSuit.Diamonds),
        ],
    ])
    def test_brelan(self, hand):
        assert (check_score(hand) == 50)