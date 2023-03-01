import random

def get_computer_choice() -> str:
    """
    Randomly select rock, paper, or scissors
    """
    return random.choice("RPS")

def compare(u_choice: str, c_choice: str) -> str:
    """
    Check to see who wins the game. Returns string with outcome.
    """
    outcome = "Loss"
    if u_choice == c_choice:
        outcome = "Tie"
    elif ((u_choice == "R" and c_choice == "S") or
          (u_choice == "P" and c_choice == "R") or
          (u_choice == "S" and c_choice == "P")):
        outcome = "Win"
    
    return outcome

def test():
    print(get_computer_choice())
    print(get_computer_choice())
    print(get_computer_choice())
    print(compare("R", "R"))
    print(compare("R", "P"))
    print(compare("R", "S"))
    # etc

def main():
    user = input("Choose between R, P, S: ")
    computer = get_computer_choice()
    result = compare(user, computer)
    print(f"You chose {user}, computer chose {computer}. "
          f"That's a {result}!")

# test()
main()