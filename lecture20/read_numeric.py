def read_int_data(filename: str) -> list:
    """
    Reads a list of integers from filename.
    """
    nums = []
    f = open(filename, "r")
    for line in f:
        num = int(line)
        nums.append(num)
    f.close()
    return nums

def main() -> None:
    nums = read_int_data("data/numeric_data.txt")
    print(nums)
    print(sum(nums))

main()