def read_int_data(filename: str) -> list:
    """
    Reads a list of integers from filename.
    """
    nums = []
    try:
        f = open(filename, "r")
        for line in f:
            try:
                num = int(line)
                nums.append(num)
            except ValueError:
                pass
            
        f.close()
    except OSError:
        print(f"Could not read {filename}")

    return nums

def main() -> None:
    nums = read_int_data("data/messy_data.txt")
    print(nums)
    print(sum(nums))

main()