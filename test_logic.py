import pytest
import logic

def test_dealt_tiles_total_correctly():
    hands, deck = logic.deal_tiles()
    assert len(deck) + len(hands[0]) + len(hands[1]) + len(hands[2]) + len(hands[3]) == 148
    assert len(hands[0]) == 14
    assert len(hands[1]) == 13
    assert len(hands[2]) == 13
    assert len(hands[3]) == 13

def test_first_round_bonus_tiles():
    """Tests that bonus tiles are drawn correctly when there are no additional bonus tiles drawn"""
    hands = [
        ['🀀','🀈','🀇','🀤','🀔','🐛','🀁','🀄️','🀅','🀋','🀖','🀕','🀂','🀊'],
         ['🀄️','🀎','🀉','🀃','🀎','🀐','🐓','🀘','🀆','🀈','🀌','🀜','🀉'],
         ['🀣','🀌','🀊','🀖','🀞','🀇','🀦','🀟','🀅','🀞','🀁','🀚','🀗'],
         ['🀎','🀕','🀌','🀄️','🀂','🀎','🀂','🀛','🀠','🀋','🀧','🀞','🀠']
    ]
    deck = ['🀎','🀕','🀌','🀄️','🀂','🀎','🀂','🀛','🀠']

    hands, deck, bonus_tiles, messages = logic.draw_bonus_tiles(hands, deck)

    assert hands[0] == ['🀀','🀈','🀇','🀔','🀁','🀄️','🀅','🀋','🀖','🀕','🀂','🀊','🀠','🀛']
    assert hands[1] == ['🀄️','🀎','🀉','🀃','🀎','🀐','🀘','🀆','🀈','🀌','🀜','🀉','🀂']
    assert hands[2] == ['🀌','🀊','🀖','🀞','🀇','🀟','🀅','🀞','🀁','🀚','🀗','🀎','🀂']
    assert hands[3] == ['🀎','🀕','🀌','🀄️','🀂','🀎','🀂','🀛','🀠','🀋','🀞','🀠','🀄️']

    assert deck == ['🀎','🀕','🀌']

    assert bonus_tiles[0] == ['🀤','🐛']
    assert bonus_tiles[1] == ['🐓']
    assert bonus_tiles[2] == ['🀣','🀦']
    assert bonus_tiles[3] == ['🀧']
