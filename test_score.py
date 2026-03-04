import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score

def test_add_points(game):
    result = add_points(game,20)
    assert result["score"] == 20

def test_add_points_negative(game):
    with pytest.raises(ValueError):
        add_points(game,-10)

def test_add_points_inactive(game):
    game["active"] = False
    result = add_points(game,20)
    assert result["score"] == 0 

def test_apply_multiplier_negative(game):
    with pytest.raises(ValueError):
        apply_multiplier(game,0)

def test_apply_multiplier_inactive(game):
    game["active"] = False
    result = apply_multiplier(game,2)
    assert result["multiplier"] == 1 

def test_apply_multiplier(game):
    result = apply_multiplier(game,2)
    assert result["multiplier"] == 3

def test_reset_score(game2):
    result = reset_score(game2)
    assert result["score"] == 0

def test_is_high_score(game2):
    result = is_high_score(game2,30)
    assert result == True