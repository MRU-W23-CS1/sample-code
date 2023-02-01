import random

def roll_die() -> int:
    """
    Roll a single die.
    """
    return random.randint(1, 6)

def calc_score() -> int:
    """
    Calculates the score for a single turn.
    """
    return roll_die() * 2

def play_game(player_num: int) -> int:
    name = input(f"Enter the name of player {player_num}: ")
    dice_roll = calc_score()
    print(f"The score for {name} is {dice_roll}")

def main() -> None:
    play_game(1)
    play_game(2)

main()

# player1 = input("Enter the name of player 1: ")
# player2 = input("Enter the name of player 2: ")
# dice_roll1 = random.randint(1, 6) + random.randint(1, 6)
# print(f"The score for {player1} is {dice_roll1}")
# dice_roll2 = random.randint(1, 6) + random.randint(1, 6)
# print(f"The score for {player2} is {dice_roll2}")
