import random_utils

def generate_random_number(start, end):
    """
    Generate a random number between start and end (inclusive).
    """
    return random.randint(start, end)

def pick_random_item(items):
    """
    Pick a random item from a list.
    """
    if not items:
        return None
    return random.choice(items)

def shuffle_items(items):
    """
    Shuffle a list of items and return it.
    """
    shuffled_items = items[:]
    random.shuffle(shuffled_items)
    return shuffled_items
