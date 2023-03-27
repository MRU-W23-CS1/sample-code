def get_valid_num() -> float:
    """
    Repeatedly prompt the user to enter a number until a valid one.
    """
    prompt = "Please enter a number, or # to cancel: "
    num_str = input(prompt)
    num = 0
    while num_str != "#":
        try:
            num = float(num_str)
            num_str = "#"
        except ValueError:
            print(f"Sorry, {num_str} is not a number")
            num_str = input(prompt)
    
    return num

def true_input() -> float:
    """
    Somewhat controversial, but doesn't default to 0.
    """
    while True:
        prompt = "Please enter a number: "
        num_str = input(prompt)
        try:
            num = float(num_str)
            return num
        except ValueError:
            print(f"Sorry, {num_str} is not a number")



def main() -> None:
    # num = get_valid_num()
    num = true_input()
    print("Yay, you entered", num)

main()