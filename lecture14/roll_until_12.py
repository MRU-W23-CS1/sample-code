import random

def roll_dice() -> int:
    return random.randint(1, 6) + random.randint(1, 6)

def count_rolls() -> int:
    """
    Rolls until we get a 12, then returns count.
    """
    value = roll_dice()
    count = 1
    while value != 12:
        print(count, value)
        count = count + 1
        value = roll_dice()
    
    return count

def main() -> None:
    print(count_rolls())

main()