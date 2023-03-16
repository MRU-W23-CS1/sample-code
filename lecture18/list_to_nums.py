def to_int_list(num_str: str) -> list:
    """
    Converts a string of comma-separate numbers into a list of ints.
    """
    nums = []
    str_list = num_str.split(",")
    for i in range(len(str_list)):
        nums.append(int(str_list[i]))
    
    return nums

def main() -> None:
    nums_in = input("Enter a list of numbers, separated by commas: ")
    print(to_int_list(nums_in))

main()