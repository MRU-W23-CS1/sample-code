from random import randint

def draw_card() -> int:
    """
    Draws a card and returns the number of gems (0 - 15).
    25% chance of getting a card with 0.
    """
    zero = randint(1, 4) == 1
    gems = 0

    if not zero:
        gems = randint(1, 15)
    
    return gems

def play_game(n_players: int) -> None:
    """
    Draws a card, then either prints "sorry, better luck next time",
    or displays the number of gems per player and the remainder.
    """

def main() -> None:
    players = int(input("Enter the number of players: "))
    play_game(players)

main()