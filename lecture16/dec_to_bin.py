number = int(input("Enter a number between 1 and 100: "))
result = "" # accumulator

while number > 0:
    bit = 0
    if number % 2 != 0:
        bit = 1
    result = str(bit) + result # accumulation
    # alternative
    # result = f"{bit}{result}"
    number = number // 2

print(result)