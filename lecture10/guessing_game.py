import random

def game(guess: int) -> None:
    """
    Compares user guess to random number.
    """
    random_number = random.randint(1, 10)
    # test value
    # random_number = 8

    if guess == random_number:
        print("You got it!")
    else:
        print("Sorry, that's not right.")

def main() -> None:
    number = int(input("Guess a number between 1 and 10: "))
    game(number)

main()