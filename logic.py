import random

def setup_game(max_val):
    target = random.randint(1, max_val)

    # Attempts: 5 base + 1 extra per 50 numbers
    attempts = 5 + (max_val // 50)

    return target, attempts

def check_guess(target, guess):
    if guess == target:
        return "WIN"
    if guess > target:
        return "TOO HIGH"
    return "TOO LOW"

