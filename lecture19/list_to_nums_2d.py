def to_int_list(num_str: str) -> list:
    """
    Converts a string of comma-separate numbers into a list of ints.
    """
    nums = []
    str_list = num_str.split()
    for i in range(len(str_list)):
        nums.append(int(str_list[i]))
    
    return nums

def get_2d_list() -> list:
    """
    Prompts the user to enter each row of numbers at a time.
    Returns a list of lists of numbers.
    """
    grid = []
    prompt = "Enter a row of numbers, separated by whitespace: "
    in_str = input(prompt)
    while in_str != "":
        row = to_int_list(in_str)
        grid.append(row)
        in_str = input(prompt)
    
    return grid

def main() -> None:
    hard_coded = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print(hard_coded)
    two_d = get_2d_list()
    for row in two_d:
        print(row)

main()