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
    card = draw_card()
    # print(card)

    if card == 0:
        print("Better luck next time")
    else:
        num_per_player = card // n_players
        remainder = card % n_players
        print(f"Each player gets {num_per_player} gems "
            f"with {remainder} left over")

def main() -> None:
    players = int(input("Enter the number of players: "))
    play_game(players)

main()