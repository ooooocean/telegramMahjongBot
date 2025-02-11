import pytest
import logic

def test_dealt_tiles_total_correctly():
    hands, deck = logic.deal_tiles()
    assert len(deck) + len(hands[0]) + len(hands[1]) + len(hands[2]) + len(hands[3]) == 148
    assert len(hands[0]) == 14
    assert len(hands[1]) == 13
    assert len(hands[2]) == 13
    assert len(hands[3]) == 13