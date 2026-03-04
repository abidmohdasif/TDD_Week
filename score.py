def add_points(game,amount):
    if amount < 0:
        raise ValueError("Enter a positive number")
    elif game['active'] == False:
        return game
    else:
        game["score"] += amount * game['multiplier']
        return game

def apply_multiplier(game, multiplier):
    if multiplier < 1:
        raise ValueError("It has to be greater than or equal to 1")
    elif game["active"] == False:
        return game
    else:
        game["multiplier"] += multiplier
        return game

def reset_score(game2):
    game2["score"] = 0
    game2["multiplier"] = 1
    return game2

def is_high_score(game2, threshold):
    if threshold < 0:
        raise ValueError("Threshold must be greater than 0")
    if game2["score"] > threshold:
        return True
    else:
        return False

