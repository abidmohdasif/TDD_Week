def add_points(game,amount):
    game["score"] += amount
    return game

def apply_multiplier(game, multiplier):
    game["multiplier"] += multiplier
    return game

def reset_score(game):
    pass

def is_high_score(game, threshold):
    pass