def say_hello(whatever: str) -> None:
    print(f"Hello, {whatever}")
    print(whatever)

def main() -> None:
    name = input("Enter your name: ")
    say_hello(name)
    # print(whatever) # not available in this scope

main()