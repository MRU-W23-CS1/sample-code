def blink_S() -> None:
    print(" * * * ")

def blink_O() -> None:
    print(" - - - ")

def SOS() -> None:
    blink_S()
    blink_O()
    blink_S()
    print()

def main() -> None:
    print("Functions version")
    SOS()
    SOS()

main()