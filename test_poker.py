import pytest

from Model import Card, CardRank, CardSuit
from main import check_score


class TestPoker:

    @pytest.mark.parametrize('hand', [[
        Card(CardRank.one, CardSuit.Diamonds),
        Card(CardRank.one, CardSuit.Diamonds),
        Card(CardRank.one, CardSuit.Diamonds),
        Card(CardRank.one, CardSuit.Diamonds),
        Card(CardRank.nine, CardSuit.Diamonds),
    ]])
    def test_high_card(self, hand):
        assert(check_score(hand) == CardRank.nine.value)