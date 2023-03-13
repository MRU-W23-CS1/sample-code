def modify_me(a: list) -> None:
    a[0] = 0

def main() -> None:
    b = [1, 2, 3]
    modify_me(b)
    print(b)

main()