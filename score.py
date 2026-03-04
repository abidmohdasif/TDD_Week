def add_points(game,amount):
    game["score"] += amount
    return game

def apply_multiplier(game, multiplier):
    game["multiplier"] += multiplier
    return game

def reset_score(game2):
    assert game2["score"] == 0
    return game2

def is_high_score(game, threshold):
    pass