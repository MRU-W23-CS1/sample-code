def get_user_input() -> list:
    """
    Prompts the user to enter a list of integers separated by spaces.
    Casts each one to an integer and returns the list.
    (~5 lines of code)
    """
    numbers = input("Enter a list of integers separated by spaces: ")

    # Pythonic/ChatGPT solution:
    # user_list = [int(x) for x in numbers.split()]

    user_list = numbers.split()
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    return user_list

def swap(nums: list, pos1: int, pos2: int) -> None:
    """
    Prompts the user to enter a list of integers separated by spaces.
    Casts each one to an integer and returns the list.
    (~5 lines of code)
    """
    # Pythonic/ChatGPT solution:
    # nums[pos1], nums[pos2] = nums[pos2], nums[pos1]

    # More general solution:
    temp = nums[pos1]
    nums[pos1] = nums[pos2]
    nums[pos2] = temp

def loop_and_swap(nums: list) -> bool:
    """
    Loops through the list of numbers. 
    If the next value in the list is smaller than the current one, 
    swap them by calling the swap function. If any swap was done,
    return True, otherwise return False.
    (~6 lines of code)
    """
    was_swapped = False
    for i in range(len(nums) - 1):
        if nums[i] > (nums[i + 1]):
            swap(nums, i, i + 1)
            was_swapped = True
    return was_swapped

def process(nums: list) -> None:
    """
    Repeatedly calls loop_and_swap, passing nums as an argument.
    Stops when loop_and_swap returns False.
    (~3 lines of code)
    """
    # Pythonic/ChatGPT solution:
    # while loop_and_swap(nums):
    #     pass

    # More general solution:
    changing = True
    while changing:
        changing = loop_and_swap(nums)

def main():
    nums = get_user_input()
    print("Before processing:", nums)
    process(nums)
    print("After processing:", nums)

main()