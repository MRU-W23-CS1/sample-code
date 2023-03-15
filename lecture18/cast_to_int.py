def to_int(nums: list) -> list:
    """
    Converts each item in a list to an integer
    """
    for i in range(len(nums) + 1):
        nums[i] = int(nums[i])

def main() -> None:
    f_nums = [3.14, 2.5, 8.2]
    s_nums = ["4", "3", "2"]
    # mixed = [3.14, 5, "3.14", [5, 2]] # danger!
    print(f_nums)
    to_int(f_nums)
    print(f_nums)

main()