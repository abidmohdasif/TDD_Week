import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score

def test_add_points(game):
    result = add_points(game,20)
    assert result["score"] == 20

def test_apply_multiplier(game):
    result = apply_multiplier(game,2)
    assert result["multiplier"] == 3

def test_reset_score(game):
    result = reset_score(game)
    assert result["score"] == 0

def test_is_high_score(game,):
    result = is_high_score(game,50)
    assert result == True