import random

def roll_dice() -> int:
    return random.randint(1, 6) + random.randint(1, 6)

def count_12s() -> int:
    """
    Rolls 100 times, counting number of 12s.
    """
    count = 0
    twelve_counter = 0
    while count < 100:
        value = roll_dice()
        print(count, value)
        if value == 12:
            twelve_counter += 1
        count = count + 1
    
    return twelve_counter

def main() -> None:
    print(count_12s())

main()