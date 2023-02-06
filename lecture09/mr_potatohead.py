def disp(first: str, last: str) -> None:
    """Displays the name"""
    print(f"{first} {last}")

def concat(first: str, last: str) -> str:
    """Concatenates the name"""
    return f"{first} {last}"

def main() -> None:
    disp("Mr.", "Potatohead")
    name = concat("Mr.", "Potatohead")
    print(name)

main()