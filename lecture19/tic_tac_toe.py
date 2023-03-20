def greeting() -> None:
    """
    Print instructions on how to play the game.
    """

def display_board(board: list) -> None:
    """
    Display the current game board state.
    """

def get_player_choice(board: list, player: int) -> None:
    """
    Gets choice from user and validates.
    """

def update_board(board: list, choice: int, player: int) -> None:
    """
    Updates the board with player's choice
    """

def game_over(board: list) -> bool:
    """
    Checks if someone has won or game is tied
    """

def check_outcome(board: list) -> str:
    """
    Checks who won the game.
    """

def game_loop() -> str:
    """
    Primary game loop, returns outcome.
    """
    current_player = 1
    # initialize board
    while not game_over(board):
        display_board(board)
        get_player_choice(board, current_player)
        update_board(board)
        # switch player
    
    return check_outcome(board)

def main() -> None:
    """
    Main program entry point
    """
    greeting()
    outcome = game_loop()
    print(outcome)

main()