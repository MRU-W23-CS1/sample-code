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
    elif guess < random_number:
        print("Sorry, your number is too low")
    elif guess > random_number:
        print("Sorry, your number is too high")
    else:
        print("This should never happen!")

def main() -> None:
    number = int(input("Guess a number between 1 and 10: "))
    game(number)

main()