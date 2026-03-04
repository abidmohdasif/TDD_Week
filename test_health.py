from health import *

def test_take_damage(player):
    result = take_damage(player, 30)
    assert result["health"] == 70

def test_add_damage(player):
    result = take_damage(player, 30)
    result = heal(player, 30)
    assert result["health"] == 100

def test_is_alive_true(player):
    result = take_damage(player, 100)
    assert is_alive(result) == False

def test_add_points(new_game):
    result = add_points(new_game, 10)
    assert result["score"] == 10
    