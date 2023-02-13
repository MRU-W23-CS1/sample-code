def correct_order(caffeine: float) -> None:
    if caffeine > 200:
        print("TOO MUCH!")
    elif caffeine > 100:
        print("Perfect amount")
    elif caffeine > 50:
        print("Good start")
    else:
        print("You need more!")

def reverse_order(caffeine: float) -> None:
    if caffeine > 50:
        print("Good start")
    elif caffeine > 100:
        print("Perfect amount")
    elif caffeine > 200:
        print("TOO MUCH!")
    else:
        print("You need more!")


def main() -> None:
    correct_order(1000)
    reverse_order(1000)

main()