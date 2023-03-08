import random

TARGET = random.randint(1,10)
# TARGET = 7

def get_valid_input(prompt: str) -> int:
    number = int(input(prompt))
    while number < 1 or number > 10:
        print(f"{number} is not between 1 and 10!")
        number = int(input(prompt))
    
    return number

def play_game() -> None:
    number = get_valid_input("Guess a number between 1 and 10: ")
    guesses = 1
    # while number != TARGET or guesses != 3: # intuitive compound condition
    while number != TARGET and guesses != 3:
        number = get_valid_input("Sorry, guess again: ")
        guesses += 1

    if number == TARGET:
        print(f"You guessed {TARGET} in {guesses} guesses!")
    else:
        print("Sorry, you're out of guesses")
    
def main() -> None:
    play_game()
    # test get_valid_input alone
    # number = get_valid_input("Guess a number between 1 and 10: ")

main()