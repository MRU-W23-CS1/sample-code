def find_largest_while(nums: list) -> int:
    """
    Returns the largest number
    in the list nums
    """
    largest = nums[0] # accumulator
    i = 0 # LCV
    while i < len(nums):
        if nums[i] > largest:
            largest = nums[i]
        i += 1 # LCV update
    
    return largest


def find_largest_for_range(nums: list) -> int:
    """
    Returns the largest number
    in the list nums
    """
    largest = nums[0] # accumulator
    # need to make sure max value is in range
    for i in range(len(nums)): 
        if nums[i] > largest:
            largest = nums[i]
        # nums[i] = 0 # really bad side effect, don't do this
    
    return largest

def find_largest_for_sequence(nums: list) -> int:
    """
    Returns the largest number
    in the list nums
    """
    largest = nums[0] # accumulator
    for num in nums:
        if num > largest:
            largest = num
        num = 0 # doesn't affect the list
    
    print(nums)
    
    return largest

def main() -> None:
    data = [1, 3, 2, 8, 9, 13, -3, 8]
    print(f"while: {find_largest_while(data)}")
    print(f"for in range: {find_largest_for_range(data)}")
    print(f"for in sequence: {find_largest_for_sequence(data)}")

main()