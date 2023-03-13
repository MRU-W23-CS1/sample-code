def print_times_table() -> None:
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{j *i: <5}", end="")
        print()

def main() -> None:
    print_times_table()

main()