some_nums = [0, 2, 0, 0, 3, 4, 0, 0, 1, 0, 2, 5, 0, 0]
zero_counter = 0
for i in range(len(some_nums)):
    if some_nums[i] == 0:
        zero_counter += 1

print(f"There are {zero_counter} zeros")

pairs_counter = 0
for i in range(len(some_nums) - 1):
    if some_nums[i] == 0 and some_nums[i+1] == 0:
        pairs_counter += 1

print(f"There are {pairs_counter} pairs")

pairs_of_zeros = 0
for i in range(1, len(some_nums)):
    if some_nums[i] == 0 and some_nums[i - 1] == 0:
        pairs_of_zeros += 1

print(f"There are {pairs_of_zeros} pairs")