import pytest
import logic

def test_dealt_tiles_total_correctly():
    hands, deck = logic.deal_tiles()
    assert len(deck) + len(hands[0]) + len(hands[1]) + len(hands[2]) + len(hands[3]) == 148